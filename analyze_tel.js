import { Codex } from "@openai/codex-sdk";

async function main() {
  try {
    const codex = new Codex();
    console.log("Analyzing Tokyo Electron (TOELY/8035) with Codex SDK...");
    const thread = codex.startThread();
    
    const prompt = `
I need a comprehensive analysis of Tokyo Electron (Ticker: TOELY or 8035.T). 
Please perform a web search to gather the latest information on the following:

1. Recent Sentiment & Memory Supercycle: What is the current market sentiment regarding Tokyo Electron's position in the AI-driven memory (HBM/DRAM) supercycle?
2. Stock Performance: How has the stock traded over the last year? (Include approximate 1-year return and recent trends).
3. Regulatory & Policy Risk: Are there any material news items regarding export controls, China-related risks, or other geopolitical/regulatory impacts?
4. Corporate News: Any recent reports on fraud, significant insider activity, or major structural changes?
5. Innovation & CAPEX: What are the latest developments in product innovation (e.g., etch/deposition for advanced nodes), CAPEX spending, and new facilities or expansions?

Provide a detailed, structured report based on verified financial news and industry analysis.
`;

    const result = await thread.run(prompt);

    console.log("TEL_ANALYSIS_START");
    console.log(result.finalResponse);
    console.log("TEL_ANALYSIS_END");
  } catch (error) {
    console.error("Error analyzing Tokyo Electron:", error);
  }
}

main();
