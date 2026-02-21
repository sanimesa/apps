import { Codex } from "@openai/codex-sdk";
import fs from "fs";

async function main() {
  const holdingsData = fs.readFileSync("/home/aikath/.openclaw/data/fsb0.pacer.x330.QQWZ_Holdings.csv", "utf8");
  
  try {
    const codex = new Codex();
    console.log("Processing sector weights and specific holdings with Codex SDK...");
    const thread = codex.startThread();
    
    const prompt = `
I have the holdings data for the QQWZ ETF.
Please analyze the data to provide the following:

1. A breakdown of the total portfolio weight by Sector (sum the Weightings for all tickers in each sector).
2. The specific weights for the following tickers:
   - ASML
   - NVDA
   - MU (Micron)
   - AMD
   - QCOM
   - VST (Vistra)
   - SMH (or relevant Semiconductor ETFs)
   - IBIT/ETHA/Crypto proxies (if any)
3. List any other sectors that have more than 5% total weight.

Holdings Data:
${holdingsData}
`;

    const result = await thread.run(prompt);

    console.log("SECTOR_ANALYSIS_START");
    console.log(result.finalResponse);
    console.log("SECTOR_ANALYSIS_END");
  } catch (error) {
    console.error("Error analyzing sector weights:", error);
  }
}

main();
