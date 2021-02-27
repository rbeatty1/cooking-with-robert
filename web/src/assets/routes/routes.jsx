import React from "react";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Landing from "../pages/Landing/Landing";
import Recipes from "../pages/Recipes/Recipes";
const ROUTE_MAP = {
    RECIPES : "recipes",
    TECHNIQUES : "techniques",
    BLOG : "blog"
};

let router = (
    <Router>
      <Switch>
        <Route path="/" exact component={Landing} />
        <Route path="/recipes" exact component={Recipes} />
        {/* <Route path="/techniques" exact component={Techniques} /> */}
        {/* <Route path="/blogs" exact component={Blogs} /> */}
      </Switch>
    </Router>
  );

export {
    router,
    ROUTE_MAP
} 