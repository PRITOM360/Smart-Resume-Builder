import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Authentication from './components/Authentication';
import ResumeBuilder from './components/ResumeBuilder';
import AI from './components/AI';
import Analytics from './components/Analytics';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/auth" component={Authentication} />
          <Route path="/resume-builder" component={ResumeBuilder} />
          <Route path="/ai" component={AI} />
          <Route path="/analytics" component={Analytics} />
          <Route path="/" exact>
            <h1>Welcome to the Smart Resume Builder</h1>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;