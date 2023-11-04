import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
function App() {
  const [audioFile, setAudioFile] = useState(null);
  const [transcriptionFile, setTranscriptionFile] = useState(null);
  const [selectedLanguage, setSelectedLanguage] = useState('eng'); // Default to 'en' (English)
  const [outputData, setOutputData] = useState(null);

  const handleAudioFileChange = (e) => {
    setAudioFile(e.target.files[0].name);
  };

  const handleTranscriptionFileChange = (e) => {
    setTranscriptionFile(e.target.files[0].name);
  };

  const handleLanguageChange = (e) => {
    setSelectedLanguage(e.target.value);
  };

  const handleUpload = () => {
    const jsonObject = {
      audio: audioFile,
      transcription: transcriptionFile,
      language: selectedLanguage
    };

    axios.post('http://127.0.0.1:5000/api/process', jsonObject)
      .then(response => {
        setOutputData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '50vh' }}>
      <h1>Aeneas Audio Transcription</h1>
      <input type="file" accept=".wav" onChange={handleAudioFileChange} />
      <input type="file" accept=".txt" onChange={handleTranscriptionFileChange} />

      {/* Language selection dropdown */}
      <label htmlFor="language">Select Language:</label>
      <select id="language" value={selectedLanguage} onChange={handleLanguageChange}>
        <option value="eng">English</option>
        <option value="hin">Hindi</option>
        {/* <option value="es">marathi</option> */}
        {/* Add more language options as needed */}
      </select>

      <button onClick={handleUpload}>Upload and Process</button>

      {outputData && (
        <div>
          {/* <h2>JSON Output:</h2> */}
          <pre>{JSON.stringify(outputData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
