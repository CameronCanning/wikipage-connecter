import { useState } from 'react';
import './App.css';
import SearchBox from './SearchBox';
const axios = require('axios');

function App() {
	const [start, setStart] = useState('');
	const [end, setEnd] = useState('');
	const [chain, setChain] = useState([]);

	const getChain = () => {
		axios.get('link', {params: {start: start, end: end}})
		.then(res => setChain(res.data.chain));
	}


	
	return (
		<div className="App">
			<SearchBox
				setPage={setStart}/>
			<SearchBox 
				setPage={setEnd}/>
			<button onClick={getChain}>get</button>
			<div>

				{chain.reduce((prev, curr) => prev += ' ' + curr, '')}

			</div>
			
		</div>
  	);
}

export default App;
