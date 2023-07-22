import React from 'react'
import { logo } from '../assets';

export const Hero = () => {
  return (
    <header className='w-full flex justify-center items-center flex-col'>
      <nav
        className="flex justify-between items-center w-full mb-10 pt-3">
        <img src={logo} alt="sumz_logo" className='w-28 object-contain' />
        <button type="button" onClick={() => window.open('https://github.com/RizanKhan837')} className='black_btn'>
          Github
        </button>
      </nav>

        <h1 className='head_text'>
        Unleash the Sole Power<br className='max-md:hidden' />
        <span className='orange_gradient '>Your Ultimate Sneakers Scraper</span>
      </h1>
      <h2 className='desc'>Sneakers scraping tool: Python-based web scraper for gathering sneaker data from various online sources. Fast, efficient, and customizable.</h2>
    </header>
  )
}
