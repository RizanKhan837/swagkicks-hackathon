import React from 'react'
import { useState, useEffect } from 'react'
import { copy, linkIcon, loader, tick } from "../assets";
//import { FileReader } from 'react';
import APIService from './APIService.jsx';
import './static/style.css'
import './OrdersTable.jsx'
import OrdersTable from './OrdersTable.jsx';
import AnimatedCheckmark, { MODES } from 'react-animated-checkmark'
import Error404 from './error404';

export const Demo = (props) =>  {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState("");
  const [error, setError] = useState(false);
  const [mode, setMode] = useState(MODES.LOADING);
  const [sneaksData, setSneaksData] = useState([]);
  const [products, setProducts] = useState([]);

  if(error) {
    return <Error404/>
  }


  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    APIService.sendQuery(query)
        .then((response) => {
          setLoading(false);
          setResult(response.data.result);
          window.location.reload();
          //setResults(response.data.result);
        })
        .catch((error) => {
          setLoading(false);
          console.log('Error:', error);
          setError(true);
        });
  };

  let loadingAnim;


  /* console.log("This Is File", file); */
  return (

    <div>
    <section className='mt-16 w-full max-w-xl mx-auto'>

      <div className='flex flex-col w-full gap-2'>
        <form className='relative flex justify-center items-center' onSubmit={handleSubmit}>
          <img src={linkIcon} alt="link_icon" className='absolute left-0 my-2 ml-3 w-5' />
          
          <input
          type="text"
          placeholder='Enter Website URL'
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
          className='url_input peer'
        />

        <button className="Btn" type="submit" disabled={loading}>
          {loading ? (
            <div className="loader">
              <img src={loader} alt="loader" />
            </div>
          ) : (
            <>
              <div className="sign">
                <svg viewBox="0 0 512 512">
                  <path d="M377.9 105.9L500.7 228.7c7.2 7.2 11.3 17.1 11.3 27.3s-4.1 20.1-11.3 27.3L377.9 406.1c-6.4 6.4-15 9.9-24 9.9c-18.7 0-33.9-15.2-33.9-33.9l0-62.1-128 0c-17.7 0-32-14.3-32-32l0-64c0-17.7 14.3-32 32-32l128 0 0-62.1c0-18.7 15.2-33.9 33.9-33.9c9 0 17.6 3.6 24 9.9zM160 96L96 96c-17.7 0-32 14.3-32 32l0 256c0 17.7 14.3 32 32 32l64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-64 0c-53 0-96-43-96-96L0 128C0 75 43 32 96 32l64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32z"></path>
                </svg>
              </div>
              <div className="text">Submit</div>
            </>
          )}
        </button>

        </form>
      </div>
    </section>
    <OrdersTable result={result || null} />
    </div>
  )
};