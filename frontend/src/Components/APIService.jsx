
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const APIService = {
	sendQuery: (query) => {
		return axios.post(`${API_BASE_URL}/translate-query`, { query });
	  }
};

export default APIService;