import { Gist } from '../types';

const API_URL = 'https://api.github.com/gists/public';

const fetchData = async (): Promise<Gist[]> => {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data: Gist[] = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching gists:', error);
    return [];
  }
};

export default fetchData; 