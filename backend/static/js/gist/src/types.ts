export interface GistFile {
  raw_url: string;
  language: string;
  fileName?: string;
  content?: string;
}

export interface GistOwner {
  login: string;
  avatar_url: string;
}

export interface Gist {
  id: string;
  files: { [key: string]: GistFile };
  owner: GistOwner;
  created_at: string;
  description: string;
}

export interface GistListProps {
  gists: Gist[];
}

export interface GistProps {
  gist: Gist;
}

export interface RawFile {
  content: string;
  language: string;
  fileName: string;
} 