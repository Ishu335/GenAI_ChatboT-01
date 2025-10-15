
import { createContext, useState } from "react";
import runChat from "../Config/gemini";
import API from "../api";
export const Context = createContext();

const ContextProvider = (props) => {
    const [input, setInput] = useState("");
    const [recentPrompt, setRecentPrompt] = useState("");
    const [prevPrompt, setPrevPrompt] = useState([]);
    const [showResult, setShowResult] = useState(false);
    const [loading, setLoading] = useState(false);
    const [resultData, setResultData] = useState("");

    // Typing effect function hereused as useEffect
    // This function will be used to simulate typing effect by adding words one by one  
    const delayPara = (index, nextWord) => {
    setTimeout(() => {
        setResultData((prev) => prev + nextWord);
    }, 75 * index);
    };
    const filterResponse = (response) => {

        
        // Process response for bold tags
        let responseArray = response.split("**");
        let newResponse2 = "";
        for (let i = 0; i < responseArray.length; i++) {
            if (i === 0 || i % 2 !== 1) {
                newResponse2 += responseArray[i];
            } else {
                newResponse2 += "<b>" + responseArray[i] + "</b>";
            }
        }
        
        // Process for new lines
        let finalResponse = newResponse2.split("*").join("<br/>");

        // Typing effect - split the final response by words to animate
        // This will now correctly include the HTML tags for styling
        let newResponseArray = finalResponse.split(" ");
        for (let i = 0; i < newResponseArray.length; i++) {
            const nextWord = newResponseArray[i];
            delayPara(i, nextWord + " "); // Add a space back after each word
        }

    };

    const sendMessage = async (prompt) => {

        const response = await API.post("/send/prompt", {
        prompt,  // field name must match backend model
        });

        // if (!response.ok) {
        //     throw new Error("Failed to send prompt");
        // }

        
        console.log("Response received from backend:", response);
        return response.data.response
    }

    const onSent = async (prompt) => { // 'prompt' parameter is redundant if you're using 'input' state
        setResultData("");
        setLoading(true);
        setShowResult(true);
        
        // Add current input to previous prompts only if it's not empty
        if (input.trim() !== "") {
            setRecentPrompt(input);
            setPrevPrompt((prev) => [...prev, input]);
        }
        
        const response = await sendMessage(input);
        console.log("Response from sendMessage:", response);
        
        filterResponse(response);
        
        setLoading(false);
        setInput("");
    };

    const contextValue = {
        input,
        setInput,
        recentPrompt,
        setRecentPrompt,
        prevPrompt,
        setPrevPrompt,
        showResult,
        setShowResult,
        loading,
        setLoading,
        resultData,
        setResultData,
        onSent
    };

    return (
        <Context.Provider value={contextValue}>
            {props.children}
        </Context.Provider>
    );
};

export default ContextProvider;


