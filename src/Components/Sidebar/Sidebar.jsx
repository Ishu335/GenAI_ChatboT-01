
import React, { useContext, useState } from 'react';
import './Sidebar.css';
import { assets } from '../../assets/assets';
import { Context } from '../../context/Context';

const Sidebar = () => {
    const [extended, setExtended] = useState(false);
    const {
        onSent,
        prevPrompt,
        setRecentPrompt,
        setResultData,
        setInput,
        setShowResult,
        setLoading,
    } = useContext(Context);

    const loadPrompt = async (prompt) => {
        setRecentPrompt(prompt);
        setResultData("");
        setInput(prompt);
        setShowResult(true);
        setLoading(true);
        await onSent(prompt);
        setLoading(false);
    };

    const newChat = () => {
        setLoading(false);
        setShowResult(false);
        setInput("");
        setResultData("");
        setRecentPrompt("");
    };

    return (
        <div className="sidebar">
            <div className="top">
                <img
                    onClick={() => setExtended(prev => !prev)}
                    className="menu"
                    src={assets.menu_icon}
                    alt="Menu Icon"
                />
                <div className="new-chat" onClick={newChat}>
                    <img src={assets.plus_icon} alt="New Chat Icon" />
                    {extended && <p>New Chat</p>}
                </div>
                {extended && (
                    <div className="recent">
                        <p className="recent-title" id='recent_name'>Recent</p>
                        {prevPrompt.map((item, index) => (
                            <div
                                className="recent-entry"
                                key={index}
                                onClick={() => loadPrompt(item)}
                            >
                                <img src={assets.message_icon} alt="Message Icon" />
                                <p>{item.length > 18 ? item.substring(0, 20) + '...' : item}</p>
                            </div>
                        ))}
                    </div>
                )}
            </div>

            <div className="bottom">
                <div className="bottom-item recent-entry">
                    <img src={assets.question_icon} alt="Help Icon" />
                    {extended && <p>Help</p>}
                </div>
                <div className="bottom-item recent-entry">
                    <img src={assets.history_icon} alt="Activity Icon" />
                    {extended && <p>Activity</p>}
                </div>
                <div className="bottom-item recent-entry">
                    <img src={assets.setting_icon} alt="Settings Icon" />
                    {extended && <p>Setting</p>}
                </div>
            </div>
        </div>
    );
};

export default Sidebar;
