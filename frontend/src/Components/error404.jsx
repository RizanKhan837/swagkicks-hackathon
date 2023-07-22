import React from 'react';
import './static/error.css';
import { Demo } from './Demo';

const Error404 = () => {
  const handleGoBack = () => {
    window.history.back();
  };

  return (
    <div className="error-container">
      <h1 className="error-code">404</h1>
      <p className="error-message">Oops! The page you are looking for could not be found.</p>
      <button className="back-button" onClick={handleGoBack}><a href={<Demo />}>Go Back</a></button>
    </div>
  );
};

export default Error404;