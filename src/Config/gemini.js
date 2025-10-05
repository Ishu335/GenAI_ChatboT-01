import {
GoogleGenerativeAI,
HarmCategory,
HarmBlockThreshold,
} from "@google/generative-ai";

// IMPORTANT: Do NOT hardcode your API key directly in client-side code like this in a production environment.
// This is for demonstration purposes only. In a real application, fetch this securely from a backend
// or use environment variables for server-side applications.
// const API_KEY = "AIzaSyDYfhe3HMy_MM--3OfWCp-_3n_GlJ3rAs0"; // Replace with your actual API key, ideally from a secure source
const API_KEY="AIzaSyAnA0h_y57Stbf-haSF_UwSzLn7MLxD7SQ"
const MODEL_NAME = "gemini-2.5-flash";

async function runChat(prompt) {
    try {
        const genAI = new GoogleGenerativeAI(API_KEY);
        const model = genAI.getGenerativeModel({ model: MODEL_NAME });

        const generationConfig = {
            temperature: 0.9,
            topK: 1,
            topP: 1,
            maxOutputTokens: 2048,
        };

        const safetySettings = [
            {
                category: HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            {
                category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            {
                category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            {
                category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
        ];

        const chat = model.startChat({
            generationConfig,
            safetySettings,
            history: [], // You can add previous messages here for conversation context
        });

        console.log("Sending prompt:", prompt); // Log the prompt for debugging
        const result = await chat.sendMessage(prompt);
        const response = result.response;
        const responseText = response.text();
        console.log("Received response:", responseText); // Log the response for debugging

        return responseText; // Return the generated text
    } catch (error) {
        if (
            error.message &&
            error.message.includes("429")
        ) {
            return "You have exceeded your Gemini API quota. Please try again later or check your billing.";
        }
        console.error("Error running chat with Gemini API:", error);
        // You can throw the error to be handled by the calling function,
        // or return a specific error message/null depending on your application's needs.
        throw error;
    }
}

export default runChat;

// Removed the commented-out old code to keep the file clean and readable.v