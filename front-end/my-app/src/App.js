import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './AuthContext';
import OAuth from './OAuth';
import DraftForm from './DraftForm';

function App() {
    return (
        <AuthProvider>
            <Router>
                <div className="App">
                    <Routes>
                        <Route path="/" element={<OAuth />} />
                        <Route path="/create-draft" element={<DraftForm />} />
                    </Routes>
                </div>
            </Router>
        </AuthProvider>
    );
}
export default App;