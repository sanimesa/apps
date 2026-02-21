import { Codex } from "@openai/codex-sdk";

async function main() {
  try {
    const codex = new Codex();
    console.log("Starting Codex thread...");
    const thread = codex.startThread();
    
    // We'll try a search-enabled prompt
    const result = await thread.run(
      "Perform a web search for the current Bitcoin price and tell me the result."
    );

    console.log("--- Codex Response ---");
    console.log(result);
    console.log("----------------------");
  } catch (error) {
    console.error("Error running Codex SDK:", error);
  }
}

main();
