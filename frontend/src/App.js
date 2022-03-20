import { useState } from 'react';
import SearchBox from './components/SearchBox';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import styled from 'styled-components';
const axios = require('axios');

const StyledApp = styled.div`
	background-color: green;	
	margin: auto;
	text-align: center;
`

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
				<StyledApp>
					<Container fluid>
						<Row>
							<p>Chain</p>
							{chain.reduce((prev, curr) => prev += ' ' + curr, '')}
						</Row>
						<Row>
							<Col style={{backgroundColor: 'red', width:'100px'}}>
								<SearchBox
									page={start}
									setPage={setStart}/>
							</Col>
							<Col style={{backgroundColor: 'blue', width:'100px'}}>
								<button onClick={getChain}>get</button>
							</Col>
							<Col style={{backgroundColor: 'yellow'}}>
								<SearchBox 
									page={end}
									setPage={setEnd}/>
							</Col>
						</Row>
					</Container>
				</StyledApp>
		)}
	else {
		return <p>mobile</p>
	}
}

export default App;
