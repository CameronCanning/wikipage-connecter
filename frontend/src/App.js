import { useState } from 'react';
import SearchBox from './components/SearchBox';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
const axios = require('axios');

function App() {
	const [start, setStart] = useState('');
	const [end, setEnd] = useState('');
	const [chain, setChain] = useState([]);

	const getChain = () => {
		axios.get('link', {params: {start: start, end: end}})
		.then(res => setChain(res.data.chain));
	}

	const isMobile = window.innerWidth <= 500;
	if (!isMobile) {
		return (
				<Container fluid>
					<Row>
						<p>Chain</p>
						{chain.reduce((prev, curr) => prev += ' ' + curr, '')}
					</Row>
					<Row>
						<Col>
							<SearchBox
								page={start}
								setPage={setStart}/>
						</Col>
						<Col>
							<button onClick={getChain}>get</button>
						</Col>
						<Col>
							<SearchBox 
								page={end}
								setPage={setEnd}/>
						</Col>
					</Row>
				</Container>
		)}
	else {
		return <p>mobile</p>
	}
}

export default App;
