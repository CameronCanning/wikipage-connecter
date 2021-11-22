import { useState } from 'react';
const axios = require('axios');



function SearchBox({queryPages, setPage}) {
    const [searchString, setSearchString] = useState('')
    const [searchResults, setSearchResults] = useState([])  

    const handleInputChange = (e) => {
        axios.get('search', {params: {search_string: e.target.value}})
        .then(res => setSearchResults(res.data.results))
        console.log(searchResults)
		setSearchString(e.target.value);
    };


    return (
    <div>    
        <input 
            type='text'
            value={searchString}
            onChange={handleInputChange}/>
        <div>
            {searchResults.map((x,i) => 
                <div key={i}>
                    <p>{x}</p>
                </div>
            )}
        </div>
    </div>
    );
}

export default SearchBox;