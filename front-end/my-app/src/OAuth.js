import React, { useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';
import './OAuth.css';


const OAuth = () => {
    const { isAuthenticated, setAuth } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        // Check if the page is loaded with a callback path
        if (window.location.pathname === '/callback') {
            // Handle the callback logic here
            // Since we're not handling tokens, just set auth to true
            setAuth(true);
            console.log(isAuthenticated);
            navigate('/create-meeting');
        }
    }, [isAuthenticated, setAuth, navigate]);

    useEffect(() => {
        console.log(isAuthenticated); // Log the state whenever it changes
    }, [isAuthenticated]);

    const handleLogin = () => {
        // Redirect to the backend login route
        window.location.href = 'http://localhost:8000/login';
    };

    return (
        <div className="oauth-container">
            <button onClick={handleLogin} className="retro-button">Login with Google</button>
        </div>
    );

};

export default OAuth;
