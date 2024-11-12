import { useState, useEffect } from 'react'
import './App.css'

function App() {

  const [data, setData] = useState([]);

  useEffect(() => {
    async function getPets() {
      const response = await fetch('http://localhost:5000/puzzles');
      const data = await response.json();
      setData(data);
    }

    getPets();
  }, []);

  if (!data) return 'Loading...';

  return (
    <>
      <h1>Be Spelling</h1>
      <ul>
        {!data.length
          ? <p>No puzzles yet</p>
          : data.map((_, i) => 
            <li>Puzzle #{i+1}</li>
        )}
      </ul>
    </>
  )
}

export default App
