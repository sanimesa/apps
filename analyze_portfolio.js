import { Codex } from "@openai/codex-sdk";
import fs from "fs";

async function main() {
  const portfolioData = fs.readFileSync("/home/aikath/.openclaw/data/Fidelity_Investment_Option_Summary_245495235_Feb-08-2026.csv", "utf8");
  
  try {
    const codex = new Codex();
    console.log("Analyzing portfolio with Codex...");
    const thread = codex.startThread();
    
    const prompt = `
I need a detailed analysis and recommendations for the following Fidelity portfolio.
The data is from a CSV export.

Portfolio Data:
${portfolioData}

Please perform the following:
1. Summarize the overall portfolio health (Total Value, Total Gain/Loss).
2. Categorize the holdings (e.g., Tech, Energy, Semiconductors, Crypto, etc.).
3. Analyze the option strategies being used (Covered Calls, Cash Covered Puts, Credit Spreads).
4. Identify high-risk positions or significant losers.
5. Provide specific, actionable recommendations (e.g., rebalancing, rolling options, closing positions).
6. Perform a web search if needed to get current market sentiment for key holdings like NVDA, AMD, MU, and Energy sectors (XLE/CHRD/DVN/FANG).
`;

    const result = await thread.run(prompt);

    console.log("ANALYSIS_START");
    console.log(result.finalResponse);
    console.log("ANALYSIS_END");
  } catch (error) {
    console.error("Error analyzing portfolio:", error);
  }
}

main();
