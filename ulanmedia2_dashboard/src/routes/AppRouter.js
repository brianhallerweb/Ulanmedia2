//@format
import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import PrivateRoute from './PrivateRoute.js';
import Home from '../components/Home.js';
import Login from '../components/Login.js';
import whitelistHome from '../components/whitelist/Home';
import greylistHome from '../components/greylist/Home';
import blacklistHome from '../components/blacklist/Home';
import good_widgetsHome from '../components/good_widgets/Home';
import campaign_setsHome from '../components/campaign_sets/Home';
import widget_domainsHome from '../components/widget_domains/Home';
import RedirectToHome from '../components/RedirectToHome';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/" exact={true} component={Home} />
        <Route path="/login" component={Login} />
        <PrivateRoute path="/whitelist" Component={whitelistHome} />
        <PrivateRoute path="/greylist" Component={greylistHome} />
        <PrivateRoute path="/blacklist" Component={blacklistHome} />
        <PrivateRoute path="/goodwidgets" Component={good_widgetsHome} />
        <PrivateRoute path="/campaignsets" Component={campaign_setsHome} />
        <PrivateRoute path="/widgetdomains" Component={widget_domainsHome} />
        // redirect to campaigns_for_all_campaigns if url doesn't match a route
        <PrivateRoute Component={RedirectToHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
