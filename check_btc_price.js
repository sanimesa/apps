const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const MOTHERDUCK_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFpa2F0aEBnbWFpbC5jb20iLCJtZFJlZ2lvbiI6ImF3cy11cy1lYXN0LTEiLCJzZXNzaW9uIjoiYWlrYXRoLmdtYWlsLmNvbSIsInBhdCI6InNFclJPbG1ocld0VVVBY2Y3T2tMSXBIOUVhWW8zRnBiVE8waU5rcFJIREUiLCJ1c2VySWQiOiI4ZWIyNmNiMi0wMTQ4LTQxN2UtYjczZS1kN2E4NmVlYjI2ZjIiLCJpc3MiOiJtZF9wYXQiLCJyZWFkT25seSI6ZmFsc2UsInRva2VuVHlwZSI6InJlYWRfd3JpdGUiLCJpYXQiOjE3Njk5MTEzNDB9.LYwKGya3HC9evxbvQubu1M5-813T4Ly3RMWRwJfh2PM";
const STATE_FILE = path.join(__dirname, 'btc_price_state.json');

async function getBtcPrice() {
    try {
        const response = execSync('curl -s https://api.coinbase.com/v2/prices/BTC-USD/spot', { encoding: 'utf8' });
        const data = JSON.parse(response);
        return parseFloat(data.data.amount);
    } catch (error) {
        console.error('Error fetching BTC price:', error.message);
        return null;
    }
}

async function logToMotherDuck(price) {
    try {
        const sql = `ATTACH 'md:my_db' AS my_db; INSERT INTO my_db.btc_history VALUES (now(), ${price});`;
        execSync(`export motherduck_token="${MOTHERDUCK_TOKEN}" && duckdb -c "${sql}"`);
        console.log('Logged to MotherDuck.');
    } catch (error) {
        console.error('Error logging to MotherDuck:', error.message);
    }
}

async function run() {
    const currentPrice = await getBtcPrice();
    if (currentPrice === null) return;

    await logToMotherDuck(currentPrice);

    let lastPrice = null;
    if (fs.existsSync(STATE_FILE)) {
        try {
            const state = JSON.parse(fs.readFileSync(STATE_FILE, 'utf8'));
            lastPrice = state.lastPrice;
        } catch (e) {
            console.error('Error reading state file:', e.message);
        }
    }

    // Save the current price as the new last price for the next run
    fs.writeFileSync(STATE_FILE, JSON.stringify({ lastPrice: currentPrice, timestamp: Date.now() }));

    if (lastPrice !== null) {
        const diff = Math.abs(currentPrice - lastPrice);
        const percentChange = (diff / lastPrice) * 100;

        if (percentChange >= 2) {
            const direction = currentPrice > lastPrice ? 'increased' : 'decreased';
            console.log(`ALERT: Bitcoin price has ${direction} by ${percentChange.toFixed(2)}%! Current: $${currentPrice.toLocaleString()}, Previous: $${lastPrice.toLocaleString()}`);
        } else {
            console.log(`Price change (${percentChange.toFixed(2)}%) is below 2%. No alert needed. (Current: $${currentPrice})`);
        }
    } else {
        console.log(`First run with MotherDuck captured price: $${currentPrice}.`);
    }
}

run();
