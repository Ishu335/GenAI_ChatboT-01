
import { createContext, useState, useEffect } from "react";
// import runChat from "../Config/gemini"; // Remove this line as you'll be fetching from backend

export const Context = createContext();

const ContextProvider = ({ children }) => {
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Function to send prompt to your Python backend
    const sendPromptToBackend = async (prompt) => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('http://127.0.0.1:5000/ask_gemini', { // Replace with your backend URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                if (response.status === 429) {
                    throw new Error("You have exceeded your Gemini API quota. Please try again later.");
                } else {
                    throw new Error(errorData.error || "Failed to get response from Gemini.");
                }
            }

            const data = await response.json();
            return data.response; // Assuming your backend returns { "response": "..." }
        } catch (err) {
            console.error("Error sending prompt to backend:", err);
            throw err; // Re-throw to be caught by onSent
        } finally {
            setLoading(false);
        }
    };


    const onSent = async (prompt) => {
        setLoading(true);
        setError(null);
        try {
            // Call the function that sends the prompt to the backend
            const response = await sendPromptToBackend(prompt);
            setMessages((prev) => [...prev, { prompt, response }]);
        } catch (err) {
            // Error handling remains similar, but now it catches errors from the fetch call
            if (err.message && err.message.includes("429")) {
                setError("You have exceeded your Gemini API quota. Please try again later.");
            } else {
                setError(err.message || "Failed to get response from Gemini.");
            }
        } finally {
            setLoading(false);
        }
    };

    // Example: send a prompt on mount (remove or modify in production)
    // useEffect(() => {
    // onSent("HI Google"); // Or "what is react js"
    // }, []); 

    const contextValue = {
        messages,
        loading,
        error,
        onSent,
    };

    return (
        <Context.Provider value={contextValue}>
            {children}
        </Context.Provider>
    );
};

export default ContextProvider;