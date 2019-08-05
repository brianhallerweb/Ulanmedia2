//@format
import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import PrivateRoute from './PrivateRoute.js';
import Login from '../components/Login.js';
import GprsForEachPOffer from '../components/GprsForEachPOffer.js';
import colorlistHome from '../components/colorlist/Home';
import good_widgetsHome from '../components/good_widgets/Home';
import campaign_setsHome from '../components/campaign_sets/Home';
import widget_domainsHome from '../components/widget_domains/Home';
import campaigns_for_all_campaignsHome from '../components/campaigns_for_all_campaigns/Home';
import campaigns_for_good_p_widgetsHome from '../components/campaigns_for_good_p_widgets/Home';
import countries_for_all_campaignsHome from '../components/countries_for_all_campaigns/Home';
import languages_for_all_campaignsHome from '../components/languages_for_all_campaigns/Home';
import campaigns_for_one_countryHome from '../components/campaigns_for_one_country/Home';
import campaigns_for_one_languageHome from '../components/campaigns_for_one_language/Home';
import p_widgets_for_all_campaignsHome from '../components/p_widgets_for_all_campaigns/Home';
import c_widgets_for_all_campaignsHome from '../components/c_widgets_for_all_campaigns/Home';
import ads_for_all_campaignsHome from '../components/ads_for_all_campaigns/Home';
import ads_for_one_campaignHome from '../components/ads_for_one_campaign/Home';
import countries_for_one_campaignHome from '../components/countries_for_one_campaign/Home';
import languages_for_one_campaignHome from '../components/languages_for_one_campaign/Home';
import offers_for_all_campaignsHome from '../components/offers_for_all_campaigns/Home';
import offers_for_one_campaignHome from '../components/offers_for_one_campaign/Home';
import offers_for_one_flow_ruleHome from '../components/offers_for_one_flow_rule/Home';
import days_for_one_campaignHome from '../components/days_for_one_campaign/Home';
import days_for_one_p_widget_for_all_campaignsHome from '../components/days_for_one_p_widget_for_all_campaigns/Home';
import days_for_one_offer_for_all_campaignsHome from '../components/days_for_one_offer_for_all_campaigns/Home';
import months_for_one_offer_for_all_campaignsHome from '../components/months_for_one_offer_for_all_campaigns/Home';
import days_for_one_ad_for_all_campaignsHome from '../components/days_for_one_ad_for_all_campaigns/Home';
import months_for_one_ad_for_all_campaignsHome from '../components/months_for_one_ad_for_all_campaigns/Home';
import days_for_one_country_for_all_campaignsHome from '../components/days_for_one_country_for_all_campaigns/Home';
import months_for_one_country_for_all_campaignsHome from '../components/months_for_one_country_for_all_campaigns/Home';
import months_for_one_p_widget_for_all_campaignsHome from '../components/months_for_one_p_widget_for_all_campaigns/Home';
import months_for_one_c_widget_for_all_campaignsHome from '../components/months_for_one_c_widget_for_all_campaigns/Home';
import days_for_one_p_widget_for_one_campaignHome from '../components/days_for_one_p_widget_for_one_campaign/Home';
import months_for_one_p_widget_for_one_campaignHome from '../components/months_for_one_p_widget_for_one_campaign/Home';
import days_for_one_ad_for_one_campaignHome from '../components/days_for_one_ad_for_one_campaign/Home';
import months_for_one_ad_for_one_campaignHome from '../components/months_for_one_ad_for_one_campaign/Home';
import months_for_one_c_widget_for_one_campaignHome from '../components/months_for_one_c_widget_for_one_campaign/Home';
import days_for_one_c_widget_for_one_campaignHome from '../components/days_for_one_c_widget_for_one_campaign/Home';
import days_for_one_c_widget_for_all_campaignsHome from '../components/days_for_one_c_widget_for_all_campaigns/Home';
import p_widgets_for_one_campaignHome from '../components/p_widgets_for_one_campaign/Home';
import c_widgets_for_one_campaignHome from '../components/c_widgets_for_one_campaign/Home';
import c_widgets_for_one_p_widget_for_one_campaignHome from '../components/c_widgets_for_one_p_widget_for_one_campaign/Home';
import c_widgets_for_one_p_widgetHome from '../components/c_widgets_for_one_p_widget/Home';
import campaigns_for_one_p_widgetHome from '../components/campaigns_for_one_p_widget/Home';
import campaigns_for_one_c_widgetHome from '../components/campaigns_for_one_c_widget/Home';
import campaigns_for_one_adHome from '../components/campaigns_for_one_ad/Home';
import campaigns_for_one_offerHome from '../components/campaigns_for_one_offer/Home';
import p_widgets_for_all_campaignsListPWidgetConfirmation from '../components/p_widgets_for_all_campaigns/ListPWidgetConfirmation';
import c_widgets_for_all_campaignsListCWidgetConfirmation from '../components/c_widgets_for_all_campaigns/ListCWidgetConfirmation';
import campaigns_for_one_p_widgetExcludeCampaignForOnePWidgetConfirmation from '../components/campaigns_for_one_p_widget/ExcludeCampaignForOnePWidgetConfirmation';
import campaigns_for_one_c_widgetExcludeCampaignForOneCWidgetConfirmation from '../components/campaigns_for_one_c_widget/ExcludeCampaignForOneCWidgetConfirmation';
import p_widgets_for_all_campaignsExcludePWidgetConfirmation from '../components/p_widgets_for_all_campaigns/ExcludePWidgetConfirmation';
import c_widgets_for_all_campaignsExcludeCWidgetConfirmation from '../components/c_widgets_for_all_campaigns/ExcludeCWidgetConfirmation';
import p_widgets_for_one_domain_for_all_campaignsHome from '../components/p_widgets_for_one_domain_for_all_campaigns/Home';
import ExcludeOneCampaignForAllBlacklistedPAndCWidgets from '../components/ExcludeOneCampaignForAllBlacklistedPAndCWidgets';
import UpdateAllData from '../components/UpdateAllData';
import UpdateOneEightyData from '../components/UpdateOneEightyData';
import RedirectToHome from '../components/RedirectToHome';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/login" component={Login} />
        <PrivateRoute path="/colorlist/:color" Component={colorlistHome} />
        <PrivateRoute path="/goodwidgets" Component={good_widgetsHome} />
        <PrivateRoute path="/campaignsets" Component={campaign_setsHome} />
        <PrivateRoute path="/widgetdomains" Component={widget_domainsHome} />
        <PrivateRoute
          path="/pwidgetsforonedomainforallcampaigns/:domain"
          Component={p_widgets_for_one_domain_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/campaignsforallcampaigns"
          Component={campaigns_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/campaignsforgoodpwidgets"
          Component={campaigns_for_good_p_widgetsHome}
        />
        <PrivateRoute
          path="/countriesforallcampaigns"
          Component={countries_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/languagesforallcampaigns"
          Component={languages_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/campaignsforonecountry/:countryName"
          Component={campaigns_for_one_countryHome}
        />
        <PrivateRoute
          path="/campaignsforonelanguage/:languageName"
          Component={campaigns_for_one_languageHome}
        />
        <PrivateRoute
          path="/daysforonecampaign/:volid"
          Component={days_for_one_campaignHome}
        />
        <PrivateRoute
          path="/daysforoneofferforallcampaigns/:offerName"
          Component={days_for_one_offer_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/monthsforoneofferforallcampaigns/:offerName"
          Component={months_for_one_offer_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/daysforoneadforallcampaigns/:adImage"
          Component={days_for_one_ad_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/monthsforoneadforallcampaigns/:adImage"
          Component={months_for_one_ad_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/daysforonecountryforallcampaigns/:countryName"
          Component={days_for_one_country_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/monthsforonecountryforallcampaigns/:countryName"
          Component={months_for_one_country_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/daysforonepwidgetforallcampaigns/:pWidgetID"
          Component={days_for_one_p_widget_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/monthsforonepwidgetforallcampaigns/:pWidgetID"
          Component={months_for_one_p_widget_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/monthsforonecwidgetforallcampaigns/:cWidgetID"
          Component={months_for_one_c_widget_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/daysforonepwidgetforonecampaign/:pWidgetID/:volID/:mgidID/:name"
          Component={days_for_one_p_widget_for_one_campaignHome}
        />
        <PrivateRoute
          path="/daysforoneadforonecampaign/:adImage/:volID/:name"
          Component={days_for_one_ad_for_one_campaignHome}
        />
        <PrivateRoute
          path="/daysforonecwidgetforonecampaign/:cWidgetID/:volID/:mgidID/:name"
          Component={days_for_one_c_widget_for_one_campaignHome}
        />
        <PrivateRoute
          path="/monthsforonepwidgetforonecampaign/:pWidgetID/:volID/:mgidID/:name"
          Component={months_for_one_p_widget_for_one_campaignHome}
        />
        <PrivateRoute
          path="/monthsforoneadforonecampaign/:adImage/:volID/:name"
          Component={months_for_one_ad_for_one_campaignHome}
        />
        <PrivateRoute
          path="/monthsforonecwidgetforonecampaign/:cWidgetID/:volID/:mgidID/:name"
          Component={months_for_one_c_widget_for_one_campaignHome}
        />
        <PrivateRoute
          path="/daysforonecwidgetforallcampaigns/:cWidgetID"
          Component={days_for_one_c_widget_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/pwidgetsforonecampaign/:volid/:name"
          Component={p_widgets_for_one_campaignHome}
        />
        <PrivateRoute
          path="/cwidgetsforonecampaign/:volid/:name"
          Component={c_widgets_for_one_campaignHome}
        />
        <PrivateRoute
          path="/cwidgetsforonepwidgetforonecampaign/:volid/:pWidget/:name"
          Component={c_widgets_for_one_p_widget_for_one_campaignHome}
        />
        <PrivateRoute
          path="/pwidgetsforallcampaigns"
          Component={p_widgets_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/cwidgetsforallcampaigns"
          Component={c_widgets_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/cwidgetsforonepwidget/:pWidgetID"
          Component={c_widgets_for_one_p_widgetHome}
        />
        <PrivateRoute
          path="/campaignsforonepwidget/:pWidgetID"
          Component={campaigns_for_one_p_widgetHome}
        />
        <PrivateRoute
          path="/campaignsforoneoffer/:offerID/:offerName"
          Component={campaigns_for_one_offerHome}
        />
        <PrivateRoute
          path="/offersforallcampaigns"
          Component={offers_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/offersforonecampaign/:volID/:campaignName"
          Component={offers_for_one_campaignHome}
        />
        <PrivateRoute
          path="/offersforoneflowrule/:flowRule"
          Component={offers_for_one_flow_ruleHome}
        />
        <PrivateRoute
          path="/campaignsforonecwidget/:widgetID"
          Component={campaigns_for_one_c_widgetHome}
        />
        <PrivateRoute
          path="/adsforonecampaign/:volid/:name"
          Component={ads_for_one_campaignHome}
        />
        <PrivateRoute
          path="/countriesforonecampaign/:volid/:name"
          Component={countries_for_one_campaignHome}
        />
        <PrivateRoute
          path="/languagesforonecampaign/:volid/:name"
          Component={languages_for_one_campaignHome}
        />
        <PrivateRoute
          path="/adsforallcampaigns"
          Component={ads_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/campaignsforonead/:adImage"
          Component={campaigns_for_one_adHome}
        />
        <PrivateRoute
          path="/listpwidgetconfirmation/:pWidgetID/:listType"
          Component={p_widgets_for_all_campaignsListPWidgetConfirmation}
        />
        <PrivateRoute
          path="/listcwidgetconfirmation/:cWidgetID/:listType"
          Component={c_widgets_for_all_campaignsListCWidgetConfirmation}
        />
        <PrivateRoute
          path="/excludecampaignforonepwidgetconfirmation/:pWidgetID/:mgidCampaignID"
          Component={
            campaigns_for_one_p_widgetExcludeCampaignForOnePWidgetConfirmation
          }
        />
        <PrivateRoute
          path="/excludecampaignforonecwidgetconfirmation/:cWidgetID/:mgidCampaignID"
          Component={
            campaigns_for_one_c_widgetExcludeCampaignForOneCWidgetConfirmation
          }
        />
        <PrivateRoute
          path="/excludepwidgetconfirmation/:pWidgetID"
          Component={p_widgets_for_all_campaignsExcludePWidgetConfirmation}
        />
        <PrivateRoute
          path="/excludecwidgetconfirmation/:cWidgetID"
          Component={c_widgets_for_all_campaignsExcludeCWidgetConfirmation}
        />
        <PrivateRoute
          path="/excludeonecampaignforallblacklistedpandcwidgets"
          Component={ExcludeOneCampaignForAllBlacklistedPAndCWidgets}
        />
        <PrivateRoute path="/updatealldata" Component={UpdateAllData} />
        <PrivateRoute
          path="/updateoneeightydata"
          Component={UpdateOneEightyData}
        />
        <PrivateRoute
          path="/gprsforeachpoffer/:dateRange"
          Component={GprsForEachPOffer}
        />
        // redirect to campaigns_for_all_campaigns if url doesn't match a route
        <PrivateRoute Component={RedirectToHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
