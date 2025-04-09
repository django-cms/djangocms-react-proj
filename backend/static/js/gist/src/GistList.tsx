import React from 'react';
import { Link } from 'react-router-dom';
import { GistListProps } from './types';

const GistList: React.FC<GistListProps> = ({ gists }) => {
  return (
    <ul className="gistList">
      {gists.map((gist, index) => (
        <li key={index} className="gist-item">
          <Link to={`/gist/${gist.id}`}>
            <img
              src={gist.owner.avatar_url}
              alt={gist.owner.login}
              className="avatarImg"
            />
            {gist.description || 'No description'}
          </Link>
        </li>
      ))}
    </ul>
  );
};

export default GistList; 