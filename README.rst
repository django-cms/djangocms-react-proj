Making React a First-Class Citizen in Django CMS with React Router Integration
===============================================================================

Introduction
------------

Django CMS is a powerful content management system that excels at structured, editorial content.
However, modern frontend experiences often demand the flexibility and interactivity of React.

In this post, we'll walk through how React — along with React Router — can be integrated as
first-class citizens in a Django CMS project, so that your editors and frontend engineers
can both thrive.

Why Integrate React with Django CMS
-----------------------------------

- Django CMS provides content structure, versioning, and editorial workflows.
- React enables interactive, dynamic UIs with modern developer ergonomics.
- Common use cases:

  - Embedding a dashboard or widget inside CMS-managed pages.
  - Creating fully dynamic web apps that live at certain CMS-defined routes.
  - Building reusable React-based plugins inside Django CMS placeholders.

Approach Overview
-----------------

There are two major strategies:

- **SPA-in-CMS:** Let Django CMS render the base HTML layout and inject React into a placeholder.
- **CMS-in-SPA:** Use Django CMS as a headless backend and build everything with React.

In this guide, we'll use the **SPA-in-CMS** approach, where React is bootstrapped inside
a Django CMS placeholder and React Router manages the internal routing.

Project Setup
-------------

1. Setup Django CMS (you can use `djangocms-installer` or your custom setup).
2. Create a React app:

   - With `create-react-app`, Vite, or Webpack.
3. Integrate using either:

   - `django-webpack-loader` (Webpack),
   - or `django-vite`.

Serving React from Django CMS
-----------------------------

- Create a Django CMS plugin that renders a `<div id="react-root"></div>` in a placeholder.
- This div acts as the mounting point for the React app.
- Your CMS template might look like:

  .. code-block:: html

     {% load render_placeholder %}
     <html>
       <body>
         {% render_placeholder "main" %}
         <script src="{% render_bundle 'main' %}"></script>
       </body>
     </html>

- You can also pass page or context data from the backend to React via `data-*` attributes or global JS variables.

React Router Configuration
--------------------------

- Wrap your React app with `<BrowserRouter>` or `<HashRouter>`.
- Configure a base path if the React app lives under a CMS-defined URL like `/app/`.
- Example:

  .. code-block:: jsx

     import { BrowserRouter, Routes, Route } from 'react-router-dom';

     const App = () => (
       <BrowserRouter basename="/app">
         <Routes>
           <Route path="/" element={<Home />} />
           <Route path="profile" element={<Profile />} />
         </Routes>
       </BrowserRouter>
     );

Handling Routing Conflicts
--------------------------

- Prevent Django from trying to resolve React's client-side routes.
- Add a CMS page with the URL `/app/` and insert your React plugin there.
- Any sub-routes like `/app/profile` will be handled by React Router.

Advanced Considerations
-----------------------

- **SEO/SSR**: React apps are client-side rendered; for SEO-heavy use cases, consider SSR or pre-rendering.
- **i18n**: Pass `language_code` from Django CMS to React, and use libraries like `react-i18next`.
- **Context sync**: Provide CMS context to React via props, global config, or context providers.

Example Configuration Snippets
------------------------------

- **Webpack:**

  .. code-block:: js

     // webpack.config.js
     output: {
       publicPath: '/static/webpack_bundles/',
     }

- **settings.py:**

  .. code-block:: python

     INSTALLED_APPS += ['webpack_loader']
     WEBPACK_LOADER = {
         'DEFAULT': {
             'BUNDLE_DIR_NAME': 'webpack_bundles/',
             'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
         }
     }

- **CMS Template:**

  .. code-block:: html

     <div id="react-root"></div>

- **React App Entry:**

  .. code-block:: js

     import ReactDOM from 'react-dom/client';
     import App from './App';

     const root = document.getElementById('react-root');
     ReactDOM.createRoot(root).render(<App />);

Deployment Tips
---------------

- Run `npm run build` (or Vite equivalent).
- Collect static files via `collectstatic`.
- Optionally serve assets via CDN.
- Avoid client/server routing conflicts by keeping React confined under predictable base paths.

Conclusion
----------

By carefully integrating React into Django CMS via placeholders and using React Router for
client-side navigation, you can build rich, dynamic UIs within an editorially friendly platform.

This hybrid setup lets you enjoy the best of both worlds — clean backend content structure
and dynamic, reactive frontends.

Optional Appendix
-----------------

- Example repo link (if any)
- Troubleshooting:

  - Missing static files?
  - Routing conflicts?
  - React Router not picking up URL paths?

- Future ideas:

  - Use of Next.js or RSC (React Server Components).
  - CMS-driven metadata injection for SSR.
