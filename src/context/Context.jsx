import { createContext, useState } from "react"; // Add useState here
import runChat from "../Config/gemini";

export const Context = createContext();

const ContextProvider = (props) => {
    const [input, setInput] = useState("");
    const [recentPrompt, setRecentPrompt] = useState("");
    const [prevPrompt, setPrevPrompt] = useState([]);
    const [showResult, setShowResult] = useState(false);
    const [loading, setLoading] = useState(false);
    const [resultData, setResultData] = useState("");

    const onSent = async (prompt) => {
        setResultData("");
        setLoading(true);
        setShowResult(true);
        const response=await runChat(input);
        setResultData(response);
        setLoading(false);
        setInput("");
        // setRecentPrompt(input);
        // await runChat(input);
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
        <Context.Provider value={contextValue}>{props.children}</Context.Provider>
    );
};
export default ContextProvider;