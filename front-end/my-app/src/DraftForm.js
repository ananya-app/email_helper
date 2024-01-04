import React, { useState, useContext, useEffect } from 'react';
import axios from 'axios';
import './DraftForm.css';

const DraftForm = () => {
    const [inputText, setInputText] = useState('');
    const [editableText, setEditableText] = useState(''); // State for editable processed text
    const [mailto, setMailto] = useState('');
    const [subject, setSubject] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [progress, setProgress] = useState(0);

    useEffect(() => {
        // Update progress based on form completion
        let newProgress = 0;
        if (inputText) newProgress += 33;
        if (mailto) newProgress += 33;
        if (subject) newProgress += 34;
        setProgress(newProgress);
    }, [inputText, mailto, subject]); 

    const handleTextSubmit = async () => {
        setIsLoading(true);
        try {
            const response = await axios.post('http://localhost:8000/process_text', { text: inputText });
            setEditableText(response.data.user_text); // Set the processed text as editable
            setIsLoading(false);
        } catch (error) {
            console.error('Error processing text:', error);
            setIsLoading(false);
        }
    };

    const handleDraftSubmit = async () => {
        setIsLoading(true);
        try {
            await axios.post('http://localhost:8000/create_draft/', {
                mailto,
                subject,
                text: editableText
            });
            alert('Draft created successfully!');
            setIsLoading(false);
        } catch (error) {
            console.error('Error creating draft:', error);
            setIsLoading(false);
        }
    };

    return (
        <div className="draft-form-container">
            <div className="progress-bar">
                <div className="progress" style={{ width: `${progress}%` }}></div>
            </div>

            <div className="prompt-message">
                <p>Enter email message:</p>
            </div>

            <textarea
                className="text-area"
                placeholder="Enter your text here..."
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
            />
            <button onClick={handleTextSubmit} disabled={isLoading}>
                {isLoading ? 'Processing...' : 'Process Text'}
            </button>

            {editableText && (
                <>
                    <textarea
                        value={editableText}
                        onChange={(e) => setEditableText(e.target.value)}
                    />
                    <input
                        type="email"
                        value={mailto}
                        onChange={(e) => setMailto(e.target.value)}
                        placeholder="Recipient's Email"
                    />
                    <input
                        type="text"
                        value={subject}
                        onChange={(e) => setSubject(e.target.value)}
                        placeholder="Email Subject"
                    />
                    <button onClick={handleDraftSubmit} disabled={isLoading}>
                        {isLoading ? 'Creating...' : 'Create Draft'}
                    </button>
                </>
            )}
        </div>
    );
};

export default DraftForm;
