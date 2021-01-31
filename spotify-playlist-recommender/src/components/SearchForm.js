import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const SearchForm = (props) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [errorMsg, setErrorMsg] = useState('');

  const handleInputChange = (event) => {
    const searchTerm = event.target.value;
    setSearchTerm(searchTerm);
  };

  const getURI = (event) => {
    console.log("in early getURI");
    //fetch('/gets').then(res => res.json()).then(data => {setSearchTerm(data)});
    console.log("in getURI");

    //giving arbitary uri
    setSearchTerm("37i9dQZF1DX0XUsuxWHRQd")
    console.log(searchTerm);
  };

  const handleSearch = (event) => {
    event.preventDefault();

    if (searchTerm.trim() !== '') {
      setErrorMsg('');
      props.handleSearch(searchTerm);
    } else {
      setErrorMsg('Please enter a search term.');
    }
  };

  return (
    <div>
        {/* <h2>Click below so you can find out which Spotify playlist most represents you!</h2> */}
      <Form onSubmit={getURI}>
      {/* <Form onSubmit={handleSearch}>
        {errorMsg && <p className="errorMsg">{errorMsg}</p>}
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Click below so you can find out which Spotify playlist most represents you!</Form.Label>
          <Form.Control
            type="search"
            name="searchTerm"
            value={searchTerm}
            placeholder="Search for album, artist or playlist"
            onChange={handleInputChange}
            autoComplete="off"
          />
          </Form.Group> */}
        <Button variant="info" type="submit" onSubmit={getURI}
        onClick={getURI}>
          Find your playlist!
        </Button>
      </Form>
    </div>
  );
};

export default SearchForm;
