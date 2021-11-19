import { useState } from 'react';
import './App.css';

const axios = require('axios');

const FLASK_URL = 'http://localhost:5000'
function App() {
	const [start, setStart] = useState('Canada');
	const [end, setEnd] = useState('Almond');
	const [chain, setChain] = useState([]);

	const getChain = () => {
		axios.get('link', {params: {'start': start, 'end': end}})
		.then(res => setChain(res.data.chain))
	}
	return (
		<div className="App">
			<input 
				type='text'
				value={start}
				onChange={(e) => setStart(e.target.value)}/>	
			<input 
				type='text'
				value={end}
				onChange={(e) => setEnd(e.target.value)}/>
			<button onClick={getChain}>get</button>
			{chain.map(x => <p key={x}>{x}</p>)}

		</div>
  	);
}

export default App;
