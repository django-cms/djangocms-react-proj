import React, { Fragment, useState, useEffect, useTransition } from 'react';
import { Link } from 'react-router-dom';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { dark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import Moment from 'moment';
import Loader from './Loader';
import { GistProps, RawFile } from './types';

const Gist: React.FC<GistProps> = ({ gist }) => {
  const [allRawFiles, setAllRawFiles] = useState<RawFile[] | null>(null);
  const [language, setLanguage] = useState<string | null>(null);
  const [content, setContent] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  useEffect(() => {
    if (!gist) {
      return;
    }

    startTransition(() => {
      const allFiles = Object.values(gist.files);
      const allRawFilesArray: RawFile[] = [];
      
      allFiles.forEach((file) => {
        const raw_url = file.raw_url;
        const fileName = file.raw_url.split('/')[file.raw_url.split('/').length - 1];
        
        fetch(raw_url)
          .then(response => response.text())
          .then(content => {
            allRawFilesArray.push({
              content: content,
              language: file.language,
              fileName: decodeURIComponent(fileName),
            });
            setContent(content);
            setLanguage(file.language);
          });
      });
      
      setAllRawFiles(allRawFilesArray);
    });
  }, [gist]);

  if (!gist) {
    return (
      <div className="alert alert-danger">
        This gist is not available anymore. <Link to="/">Go home</Link>.
      </div>
    );
  }

  const allFiles = allRawFiles;
  let allFilesContainer = null;
  
  if (allFiles !== null) {
    allFilesContainer = allFiles.map((fileObject, key) => (
      <div key={key}>
        <pre>{fileObject.fileName}</pre>
        <SyntaxHighlighter language={fileObject.language} style={dark}>
          {fileObject.content}
        </SyntaxHighlighter>
      </div>
    ));
  }

  return (
    <div className="gistResultContainer">
      <h3>{gist.owner.login} shared the gist:</h3>
      <small>
        <pre>Created on {Moment(gist.created_at).format('LLL')}</pre>
      </small>
      <pre>{gist.description}</pre>
      {isPending && (
        <Fragment>
          <p> Please wait, loading gist</p> <Loader />{' '}
        </Fragment>
      )}
      {!isPending && allFilesContainer}
    </div>
  );
};

export default Gist; 