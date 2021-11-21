import { useState } from 'react';


function SearchBox({queryPages, setPage}) {
    const [query, setQuery] = useState('')
    const [queryResults, setQueryResults] = useState([])  

    const handleInputChange = (e) => {
		setQuery(e.target.value);
        setPage(e.target.value);
        setQueryResults(e.target.value.split(''));

        setPage(e.target.value);
    };

    
    return (
    <div>    
        <input 
            type='text'
            value={query}
            onChange={handleInputChange}/>
        <div>
            {queryResults.map((x,i) => 
                <div key={i}>
                    <p>{x}</p>
                </div>
            )}
        </div>
    </div>
    );
}

export default SearchBox;