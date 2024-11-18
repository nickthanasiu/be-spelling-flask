import { useState, useEffect } from 'react'
import './App.css'

interface Puzzle {
  letters:      string[];
  centerLetter: string;
  date:         any;
}

function App() {
  const [puzzles, setPuzzles] = useState<Puzzle[]>();

  useEffect(() => {
    (async function() {
      const response = await fetch('http://localhost:5000/puzzles');
      const _puzzles: Puzzle[] = await response.json();
      setPuzzles(_puzzles);
    })()
  }, []);

  if (!puzzles) return 'Loading...';
  
  return (
    <>
      <h1>Be Spelling</h1>
      <ul>
        {!puzzles.length
          ? <p>No puzzles yet</p>
          : puzzles.map(p => 
            <li>

              <p>Center Letter: {p.centerLetter}</p>
              <p>Letters: {p.letters.map(l => l).join(', ')}</p>
            </li>
        )}
      </ul>
    </>
  )
}

export default App
