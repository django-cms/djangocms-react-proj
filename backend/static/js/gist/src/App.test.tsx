import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders gist dashboard link', () => {
  render(<App />);
  const linkElement = screen.getByText(/gist dashboard/i);
  expect(linkElement).toBeInTheDocument();
}); 