import { useState } from 'react';
import styled from 'styled-components';
const axios = require('axios');

const PageInput = styled.input`

`
const Results = styled.div`
    padding: 0px;
`
const Result = styled.div`
    outline-top: 1px solid black;
    text-align: left;
`
const SearchBoxWrapper = styled.div`

`

function SearchBox({page, setPage}) {

    const [searchResults, setSearchResults] = useState([])  

    const handleInputChange = (e) => {
        axios.get('search', {params: {string: e.target.value}})
        .then(res => setSearchResults(res.data.results))
        console.log(searchResults)
		setPage(e.target.value);
    };

    const handleKeyUp = (e) => {
        if (e.key === 'Enter') {
            changePage(0)
        }
    }

    const changePage = (i) => {
        setPage(searchResults[i])
    }

    return (
    <SearchBoxWrapper>    
        <PageInput
            type='text'
            value={page}
            onChange={handleInputChange}
            onKeyUp={handleKeyUp}/>
        <Results>
            {searchResults.map((x,i) => 
                <Result key={i} onClick={() => changePage(i)}>
                    <p>{x}</p>
                </Result>
            )}
        </Results>
    </SearchBoxWrapper>
    );
}

export default SearchBox;