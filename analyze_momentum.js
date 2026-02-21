import { Codex } from "@openai/codex-sdk";
import fs from "fs";

async function main() {
  const holdingsData = fs.readFileSync("/home/aikath/.openclaw/data/fsb0.pacer.x330.QQWZ_Holdings.csv", "utf8");
  
  try {
    const codex = new Codex();
    console.log("Analyzing QQWZ momentum holdings with Codex SDK...");
    const thread = codex.startThread();
    
    const prompt = `
I have a list of holdings for the QQWZ (Pacer NASDAQ-100 Cash Cows Growth Leaders) ETF. 
Please analyze these tickers and provide a report on their momentum factors.

Holdings Data:
${holdingsData}

Please perform the following:
1. Identify the top 10 tickers by weight in the portfolio.
2. For these top 10 (and any other significant ones like NVDA, AMD, etc.), perform a web search to find:
   - Current Market Cap
   - Sector/Industry
   - 1-Year Return (Momentum)
3. Analyze the overall "Momentum Factor" of this portfolio. Does it lean heavily into specific sectors?
4. Compare these momentum holdings with the user's current Fidelity portfolio (Energy and Semiconductors focus). Are there overlaps or diversification opportunities?
5. Identify any specific "Sector Momentum" trends visible in these holdings.

Provide the response in a clear, formatted report.
`;

    const result = await thread.run(prompt);

    console.log("MOMENTUM_ANALYSIS_START");
    console.log(result.finalResponse);
    console.log("MOMENTUM_ANALYSIS_END");
  } catch (error) {
    console.error("Error analyzing momentum holdings:", error);
  }
}

main();
