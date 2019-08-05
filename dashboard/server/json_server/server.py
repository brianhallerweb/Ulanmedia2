from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt import JWT
import os
from config.config import *
from functions.data_acquisition_functions.get_vol_access_token import get_vol_access_token
from functions.misc.create_vol_date_range import create_vol_date_range

# create datasets
from functions.data_acquisition_functions.create_p_widgets_for_all_campaigns_dataset import create_p_widgets_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_p_widget_dataset import create_campaigns_for_one_p_widget_dataset
from functions.data_acquisition_functions.create_p_widgets_for_one_campaign_dataset import create_p_widgets_for_one_campaign_dataset
from functions.data_acquisition_functions.create_p_widgets_for_one_domain_for_all_campaigns_dataset import create_p_widgets_for_one_domain_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_c_widgets_for_all_campaigns_dataset import create_c_widgets_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_c_widget_dataset import create_campaigns_for_one_c_widget_dataset
from functions.data_acquisition_functions.create_c_widgets_for_one_campaign_dataset import create_c_widgets_for_one_campaign_dataset
from functions.data_acquisition_functions.create_c_widgets_for_one_p_widget_for_one_campaign_dataset import create_c_widgets_for_one_p_widget_for_one_campaign_dataset
from functions.data_acquisition_functions.create_c_widgets_for_one_p_widget_dataset import create_c_widgets_for_one_p_widget_dataset
from functions.data_acquisition_functions.create_ads_for_all_campaigns_dataset import create_ads_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_ad_dataset import create_campaigns_for_one_ad_dataset
from functions.data_acquisition_functions.create_ads_for_one_campaign_dataset import create_ads_for_one_campaign_dataset
from functions.data_acquisition_functions.create_offers_for_all_campaigns_dataset import create_offers_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_offer_dataset import create_campaigns_for_one_offer_dataset
from functions.data_acquisition_functions.create_offers_for_one_campaign_dataset import create_offers_for_one_campaign_dataset
from functions.data_acquisition_functions.create_offers_for_one_flow_rule_dataset import create_offers_for_one_flow_rule_dataset
from functions.data_acquisition_functions.create_campaigns_for_good_p_widgets_dataset import create_campaigns_for_good_p_widgets_dataset
from functions.data_acquisition_functions.create_countries_for_all_campaigns_dataset import create_countries_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_country_dataset import create_campaigns_for_one_country_dataset
from functions.data_acquisition_functions.create_countries_for_one_campaign_dataset import create_countries_for_one_campaign_dataset
from functions.data_acquisition_functions.create_languages_for_all_campaigns_dataset import create_languages_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_language_dataset import create_campaigns_for_one_language_dataset
from functions.data_acquisition_functions.create_languages_for_one_campaign_dataset import create_languages_for_one_campaign_dataset
from functions.data_acquisition_functions.create_languages_for_one_campaign_dataset import create_languages_for_one_campaign_dataset
from functions.data_acquisition_functions.create_days_for_one_p_widget_for_all_campaigns_dataset import create_days_for_one_p_widget_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_months_for_one_p_widget_for_all_campaigns_dataset import create_months_for_one_p_widget_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_days_for_one_p_widget_for_one_campaign_dataset import create_days_for_one_p_widget_for_one_campaign_dataset
from functions.data_acquisition_functions.create_months_for_one_p_widget_for_one_campaign_dataset import create_months_for_one_p_widget_for_one_campaign_dataset
from functions.data_acquisition_functions.create_days_for_one_c_widget_for_all_campaigns_dataset import create_days_for_one_c_widget_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_months_for_one_c_widget_for_all_campaigns_dataset import create_months_for_one_c_widget_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_days_for_one_c_widget_for_one_campaign_dataset import create_days_for_one_c_widget_for_one_campaign_dataset
from functions.data_acquisition_functions.create_months_for_one_c_widget_for_one_campaign_dataset import create_months_for_one_c_widget_for_one_campaign_dataset
from functions.data_acquisition_functions.create_days_for_one_ad_for_all_campaigns_dataset import create_days_for_one_ad_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_months_for_one_ad_for_all_campaigns_dataset import create_months_for_one_ad_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_days_for_one_ad_for_one_campaign_dataset import create_days_for_one_ad_for_one_campaign_dataset
from functions.data_acquisition_functions.create_months_for_one_ad_for_one_campaign_dataset import create_months_for_one_ad_for_one_campaign_dataset
from functions.data_acquisition_functions.create_days_for_one_offer_for_all_campaigns_dataset import create_days_for_one_offer_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_months_for_one_offer_for_all_campaigns_dataset import create_months_for_one_offer_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_days_for_one_country_for_all_campaigns_dataset import create_days_for_one_country_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_months_for_one_country_for_all_campaigns_dataset import create_months_for_one_country_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_gprs_for_each_p_offer_dataset import create_gprs_for_each_p_offer_dataset

# create reports
from functions.data_analysis_functions.create_campaigns_for_all_campaigns_report import create_campaigns_for_all_campaigns_report
from functions.data_analysis_functions.create_p_widgets_for_all_campaigns_report import create_p_widgets_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_p_widget_report import create_campaigns_for_one_p_widget_report
from functions.data_analysis_functions.create_p_widgets_for_one_campaign_report import create_p_widgets_for_one_campaign_report
from functions.data_analysis_functions.create_p_widgets_for_one_domain_for_all_campaigns_report import create_p_widgets_for_one_domain_for_all_campaigns_report
from functions.data_analysis_functions.create_c_widgets_for_all_campaigns_report import create_c_widgets_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_c_widget_report import create_campaigns_for_one_c_widget_report
from functions.data_analysis_functions.create_c_widgets_for_one_campaign_report import create_c_widgets_for_one_campaign_report
from functions.data_analysis_functions.create_c_widgets_for_one_p_widget_for_one_campaign_report import create_c_widgets_for_one_p_widget_for_one_campaign_report
from functions.data_analysis_functions.create_c_widgets_for_one_p_widget_report import create_c_widgets_for_one_p_widget_report
from functions.data_analysis_functions.create_ads_for_all_campaigns_report import create_ads_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_ad_report import create_campaigns_for_one_ad_report
from functions.data_analysis_functions.create_ads_for_one_campaign_report import create_ads_for_one_campaign_report
from functions.data_analysis_functions.create_offers_for_all_campaigns_report import create_offers_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_offer_report import create_campaigns_for_one_offer_report
from functions.data_analysis_functions.create_offers_for_one_campaign_report import create_offers_for_one_campaign_report
from functions.data_analysis_functions.create_offers_for_one_flow_rule_report import create_offers_for_one_flow_rule_report
from functions.data_analysis_functions.create_campaigns_for_good_p_widgets_report import create_campaigns_for_good_p_widgets_report
from functions.data_analysis_functions.create_countries_for_all_campaigns_report import create_countries_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_country_report import create_campaigns_for_one_country_report
from functions.data_analysis_functions.create_countries_for_one_campaign_report import create_countries_for_one_campaign_report
from functions.data_analysis_functions.create_languages_for_all_campaigns_report import create_languages_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_language_report import create_campaigns_for_one_language_report
from functions.data_analysis_functions.create_languages_for_one_campaign_report import create_languages_for_one_campaign_report
from functions.data_analysis_functions.create_days_for_one_p_widget_for_all_campaigns_report import create_days_for_one_p_widget_for_all_campaigns_report
from functions.data_analysis_functions.create_months_for_one_p_widget_for_all_campaigns_report import create_months_for_one_p_widget_for_all_campaigns_report
from functions.data_analysis_functions.create_days_for_one_p_widget_for_one_campaign_report import create_days_for_one_p_widget_for_one_campaign_report
from functions.data_analysis_functions.create_months_for_one_p_widget_for_one_campaign_report import create_months_for_one_p_widget_for_one_campaign_report
from functions.data_analysis_functions.create_days_for_one_c_widget_for_all_campaigns_report import create_days_for_one_c_widget_for_all_campaigns_report
from functions.data_analysis_functions.create_months_for_one_c_widget_for_all_campaigns_report import create_months_for_one_c_widget_for_all_campaigns_report
from functions.data_analysis_functions.create_days_for_one_c_widget_for_one_campaign_report import create_days_for_one_c_widget_for_one_campaign_report
from functions.data_analysis_functions.create_months_for_one_c_widget_for_one_campaign_report import create_months_for_one_c_widget_for_one_campaign_report
from functions.data_analysis_functions.create_days_for_one_ad_for_all_campaigns_report import create_days_for_one_ad_for_all_campaigns_report
from functions.data_analysis_functions.create_months_for_one_ad_for_all_campaigns_report import create_months_for_one_ad_for_all_campaigns_report
from functions.data_analysis_functions.create_days_for_one_ad_for_one_campaign_report import create_days_for_one_ad_for_one_campaign_report
from functions.data_analysis_functions.create_months_for_one_ad_for_one_campaign_report import create_months_for_one_ad_for_one_campaign_report
from functions.data_analysis_functions.create_days_for_one_offer_for_all_campaigns_report import create_days_for_one_offer_for_all_campaigns_report
from functions.data_analysis_functions.create_months_for_one_offer_for_all_campaigns_report import create_months_for_one_offer_for_all_campaigns_report
from functions.data_analysis_functions.create_days_for_one_country_for_all_campaigns_report import create_days_for_one_country_for_all_campaigns_report
from functions.data_analysis_functions.create_months_for_one_country_for_all_campaigns_report import create_months_for_one_country_for_all_campaigns_report
from functions.data_analysis_functions.create_days_for_one_campaign_report import create_days_for_one_campaign_report

from dashboard.server.json_server.db import db
from dashboard.server.json_server.resources.colorlist import Colorlist, CompleteColorlist
from dashboard.server.json_server.resources.good_widget import GoodWidget, CompleteGoodWidgets
from dashboard.server.json_server.resources.campaign_set import CampaignSet, CompleteCampaignSets
from dashboard.server.json_server.resources.widget_domain import WidgetDomain, CompleteWidgetDomains


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://ulan:missoula1@localhost/ulanmedia"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://bsh:kensington@localhost/ulanmedia"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Colorlist, '/jsonapi/<string:color>list')
api.add_resource(CompleteColorlist, '/jsonapi/complete<string:color>list')

api.add_resource(GoodWidget, '/jsonapi/goodwidget')
api.add_resource(CompleteGoodWidgets, '/jsonapi/completegoodwidgets')

api.add_resource(CampaignSet, '/jsonapi/campaignset')
api.add_resource(CompleteCampaignSets, '/jsonapi/completecampaignsets')

api.add_resource(WidgetDomain, '/jsonapi/widgetdomain')
api.add_resource(CompleteWidgetDomains, '/jsonapi/completewidgetdomains')

#####################################
# campaigns for all campaigns

@app.route("/jsonapi/createCampaignsForAllCampaignsReport", methods=["POST"])
def createCampaignsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c5 = request.json["c5"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c7Value = request.json["c7Value"]
    c8 = request.json["c8"]
    c8Value = request.json["c8Value"]
    c9 = request.json["c9"]
    c9Value = request.json["c9Value"]
    c10 = request.json["c10"]
    c10Value = request.json["c10Value"]
    c11 = request.json["c11"]
    c11Value = request.json["c11Value"]
    c12 = request.json["c12"]
    c12Value = request.json["c12Value"]
    c13 = request.json["c13"]
    c13Value = request.json["c13Value"]
    c14 = request.json["c14"]
    c14Value = request.json["c14Value"]
    c15 = request.json["c15"]
    c15Value = request.json["c15Value"]
    c16 = request.json["c16"]
    c16Value = request.json["c16Value"]
    c17 = request.json["c17"]
    c17Value = request.json["c17Value"]
    c18 = request.json["c18"]
    c18Value = request.json["c18Value"]
    c19 = request.json["c19"]
    c19Value = request.json["c19Value"]
    c20 = request.json["c20"]
    c20Value = request.json["c20Value"]
    c21 = request.json["c21"]
    c21Value = request.json["c21Value"]
    c22 = request.json["c22"]
    c22Value = request.json["c22Value"]
    c23 = request.json["c23"]
    c23Value = request.json["c23Value"]
    c24 = request.json["c24"]
    c24Value = request.json["c24Value"]
    c25 = request.json["c25"]
    c25Value = request.json["c25Value"]
    c26 = request.json["c26"]
    c26Value = request.json["c26Value"]
    c27 = request.json["c27"]
    c27Value = request.json["c27Value"]
    return create_campaigns_for_all_campaigns_report(date_range, c1, c1Value, c2, c2Value, c3, c3Value, c4, c5, c6, c6Value, c7, c7Value, c8, c8Value, c9, c9Value, c10, c10Value, c11, c11Value, c12, c12Value, c13, c13Value, c14, c14Value, c15, c15Value, c16, c16Value, c17, c17Value, c18, c18Value, c19, c19Value, c20, c20Value, c21, c21Value, c22, c22Value, c23, c23Value, c24, c24Value, c25, c25Value, c26, c26Value, c27, c27Value)

#####################################
# p widgets for all campaigns

@app.route("/jsonapi/createPWidgetsForAllCampaignsDataset", methods=["POST"])
def createPWidgetsForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_p_widgets_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createPWidgetsForAllCampaignsReport", methods=["POST"])
def createPWidgetsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c8 = request.json["c8"]
    return create_p_widgets_for_all_campaigns_report(date_range, c1, c2, c3,
            c4, c5, c6, c7, c8, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value)

#####################################
# campaigns for one p widget

@app.route("/jsonapi/createCampaignsForOnePWidgetDataset", methods=["POST"])
def createCampaignsForOnePWidgetDataset():
    date_range = request.json["dateRange"]
    p_widget_id = request.json["pWidgetID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_campaigns_for_one_p_widget_dataset(p_widget_id, date_range, max_rec_bid)

@app.route("/jsonapi/createCampaignsForOnePWidgetReport", methods=["POST"])
def createCampaignsForOnePWidgetReport():
    date_range = request.json["dateRange"]
    p_widget_id = request.json["pWidgetID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    return create_campaigns_for_one_p_widget_report(date_range, p_widget_id, c1, c2, c3,
            c4, c5, c6, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value)

#####################################
# p widgets for one campaign

@app.route("/jsonapi/createPWidgetsForOneCampaignDataset", methods=["POST"])
def createPWidgetsForOneCampaignDataset():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_p_widgets_for_one_campaign_dataset(vol_id, date_range, max_rec_bid)

@app.route("/jsonapi/createPWidgetsForOneCampaignReport", methods=["POST"])
def createPWidgetsForOneCampaignReport():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c7Value = request.json["c7Value"]
    c8 = request.json["c8"]
    return create_p_widgets_for_one_campaign_report(date_range, vol_id, c1, c2, c3,
            c4, c5, c6, c7, c8, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value, c7Value)

#####################################
# p widgets for one domain for all campaigns

@app.route("/jsonapi/createPWidgetsForOneDomainForAllCampaignsDataset", methods=["POST"])
def createPWidgetsForOneDomainForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    domain = request.json["domain"]
    return create_p_widgets_for_one_domain_for_all_campaigns_dataset(date_range, domain)

@app.route("/jsonapi/createPWidgetsForOneDomainForAllCampaignsReport", methods=["POST"])
def createPWidgetsForOneDomainForAllCampaignsReport():
    date_range = request.json["dateRange"]
    domain = request.json["domain"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    return create_p_widgets_for_one_domain_for_all_campaigns_report(date_range,
            domain, c1, c2, c3, c4, c1Value, c2Value, c3Value, c4Value)

#####################################
# c widgets for all campaigns

@app.route("/jsonapi/createCWidgetsForAllCampaignsDataset", methods=["POST"])
def createCWidgetsForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_c_widgets_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createCWidgetsForAllCampaignsReport", methods=["POST"])
def createCWidgetsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c8 = request.json["c8"]
    return create_c_widgets_for_all_campaigns_report(date_range, c1, c2, c3,
            c4, c5, c6, c7, c8, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value)

#####################################
# campaigns for one c widget

@app.route("/jsonapi/createCampaignsForOneCWidgetDataset", methods=["POST"])
def createCampaignsForOneCWidgetDataset():
    date_range = request.json["dateRange"]
    c_widget_id = request.json["widgetID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range, max_rec_bid)

@app.route("/jsonapi/createCampaignsForOneCWidgetReport", methods=["POST"])
def createCampaignsForOneCWidgetReport():
    date_range = request.json["dateRange"]
    c_widget_id = request.json["widgetID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    return create_campaigns_for_one_c_widget_report(date_range, c_widget_id, c1, c2, c3,
            c4, c5, c1Value, c2Value, c3Value, c4Value, c5Value)

#####################################
# c widgets for one campaign

@app.route("/jsonapi/createCWidgetsForOneCampaignDataset", methods=["POST"])
def createCWidgetsForOneCampaign():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_c_widgets_for_one_campaign_dataset(vol_id, date_range, max_rec_bid)

@app.route("/jsonapi/createCWidgetsForOneCampaignReport", methods=["POST"])
def createCWidgetsForOneCampaignReport():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    return create_c_widgets_for_one_campaign_report(date_range, vol_id, c1, c2, c3,
            c4, c5, c6, c1Value, c2Value, c3Value, c4Value, c5Value)

#####################################
# c widgets for one p widget for one campaign

@app.route("/jsonapi/createCWidgetsForOnePWidgetForOneCampaignDataset", methods=["POST"])
def createCWidgetsForOnePWidgetForOneCampaignDataset():
    vol_id = request.json["volID"]
    p_widget = request.json["pWidget"]
    date_range = request.json["dateRange"]
    max_rec_bid = request.json["maxRecBid"]
    return create_c_widgets_for_one_p_widget_for_one_campaign_dataset(vol_id,
            p_widget, date_range, max_rec_bid)

@app.route("/jsonapi/createCWidgetsForOnePWidgetForOneCampaignReport", methods=["POST"])
def createCWidgetsForOnePWidgetForOneCampaignReport():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    p_widget = request.json["pWidget"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    return create_c_widgets_for_one_p_widget_for_one_campaign_report(date_range, vol_id, p_widget,  c1, c2, c3,
            c4, c5, c6, c1Value, c2Value, c3Value, c4Value, c5Value)

#####################################
# c widgets for one p widget

@app.route("/jsonapi/createCWidgetsForOnePWidgetDataset", methods=["POST"])
def createCWidgetsForOnePWidgetDataset():
    p_widget_id = request.json["pWidgetID"]
    date_range = request.json["dateRange"]
    return create_c_widgets_for_one_p_widget_dataset(p_widget_id, date_range)

@app.route("/jsonapi/createCWidgetsForOnePWidgetReport", methods=["POST"])
def createCWidgetsForOnePWidgetReport():
    date_range = request.json["dateRange"]
    p_widget_id = request.json["pWidgetID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_c_widgets_for_one_p_widget_report(date_range, p_widget_id, c1, c2, c3, c1Value, c2Value, c3Value)

#####################################
# ads for all campaigns

@app.route("/jsonapi/createAdsForAllCampaignsDataset", methods=["POST"])
def createAdsForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_ads_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createAdsForAllCampaignsReport", methods=["POST"])
def createAdsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    return create_ads_for_all_campaigns_report(date_range, c1, c2, c3, c4, c5, c1Value, c2Value, c3Value, c4Value, c5Value)

#####################################
# campaigns for one ad

@app.route("/jsonapi/createCampaignsForOneAdDataset", methods=["POST"])
def createCampaignsForOneAdDataset():
    ad_image = request.json["adImage"]
    date_range = request.json["dateRange"]
    return create_campaigns_for_one_ad_dataset(ad_image, date_range)

@app.route("/jsonapi/createCampaignsForOneAdReport", methods=["POST"])
def createCampaignsForOneAdReport():
    ad_image = request.json["adImage"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    return create_campaigns_for_one_ad_report(ad_image, date_range, c1, c2, c3, c4, c1Value, c2Value, c3Value, c4Value)

#####################################
# ads for one campaign

@app.route("/jsonapi/createAdsForOneCampaignDataset", methods=["POST"])
def createAdsForOneCampaignDataset():
    vol_id = request.json["volID"]
    date_range = request.json["dateRange"]
    return create_ads_for_one_campaign_dataset(vol_id, date_range)

@app.route("/jsonapi/createAdsForOneCampaignReport", methods=["POST"])
def createAdsForOneCampaignReport():
    vol_id = request.json["volID"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    return create_ads_for_one_campaign_report(vol_id, date_range, c1, c2, c3,
            c4, c5, c1Value, c2Value, c3Value, c4Value, c5Value)

#####################################
# offers for all campaigns

@app.route("/jsonapi/createOffersForAllCampaignsDataset", methods=["POST"])
def createOffersForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_offers_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createOffersForAllCampaignsReport", methods=["POST"])
def createOffersForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    return create_offers_for_all_campaigns_report(date_range, c1, c2, c3, c4, c5, c1Value, c2Value, c3Value, c4Value)

#####################################
# campaigns for one offer 

@app.route("/jsonapi/createCampaignsForOneOfferDataset", methods=["POST"])
def createCampaignsForOneOfferDataset():
    offer_id = request.json["offerID"]
    date_range = request.json["dateRange"]
    return create_campaigns_for_one_offer_dataset(date_range, offer_id)

@app.route("/jsonapi/createCampaignsForOneOfferReport", methods=["POST"])
def createCampaignsForOneOfferReport():
    offer_id = request.json["offerID"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_campaigns_for_one_offer_report(offer_id, date_range, c1, c2, c3, c1Value, c2Value, c3Value)

#####################################
# offers for one campaign

@app.route("/jsonapi/createOffersForOneCampaignDataset", methods=["POST"])
def createOffersForOneCampaignDataset():
    campaign_id = request.json["campaignID"]
    date_range = request.json["dateRange"]
    return create_offers_for_one_campaign_dataset(date_range, campaign_id)

@app.route("/jsonapi/createOffersForOneCampaignReport", methods=["POST"])
def createOffersForOneCampaignReport():
    campaign_id = request.json["campaignID"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_offers_for_one_campaign_report(campaign_id, date_range, c1, c2, c3,
            c1Value, c2Value, c3Value)

#####################################
# offers for one flow rule

@app.route("/jsonapi/createOffersForOneFlowRuleDataset", methods=["POST"])
def createOffersForOneFlowRuleDataset():
    flow_rule = request.json["flowRule"]
    date_range = request.json["dateRange"]
    return create_offers_for_one_flow_rule_dataset(date_range, flow_rule)

@app.route("/jsonapi/createOffersForOneFlowRuleReport", methods=["POST"])
def createOffersForOneFlowRuleReport():
    flow_rule = request.json["flowRule"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_offers_for_one_flow_rule_report(flow_rule, date_range, c1, c2, c3,
            c1Value, c2Value, c3Value)

#####################################
# campaigns for good p widgets 

@app.route("/jsonapi/createCampaignsForGoodPWidgetsDataset", methods=["POST"])
def createCampaignsForGoodPWidgetsDataset():
    date_range = request.json["dateRange"]
    max_rec_bid = request.json["maxRecBid"]
    default_coeff = request.json["defaultCoeff"]
    return create_campaigns_for_good_p_widgets_dataset(date_range, max_rec_bid, default_coeff)

@app.route("/jsonapi/createCampaignsForGoodPWidgetsReport", methods=["POST"])
def createCampaignsForGoodPWidgetsReport():
    date_range = request.json["dateRange"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_campaigns_for_good_p_widgets_report(date_range, c3, c3Value)

#####################################
# countries for all campaigns

@app.route("/jsonapi/createCountriesForAllCampaignsDataset", methods=["POST"])
def createCountriesForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_countries_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createCountriesForAllCampaignsReport", methods=["POST"])
def createCountriesForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_countries_for_all_campaigns_report(date_range, c1, c2, c3, c1Value, c2Value, c3Value)

#####################################
# campaigns for one country 

@app.route("/jsonapi/createCampaignsForOneCountryDataset", methods=["POST"])
def createCampaignsForOneCountryDataset():
    country_name = request.json["countryName"]
    date_range = request.json["dateRange"]
    return create_campaigns_for_one_country_dataset(date_range, country_name)

@app.route("/jsonapi/createCampaignsForOneCountryReport", methods=["POST"])
def createCampaignsForOneCountryReport():
    country_name = request.json["countryName"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    return create_campaigns_for_one_country_report(country_name, date_range, c1, c2, c1Value, c2Value)

#####################################
# countries for one campaign

@app.route("/jsonapi/createCountriesForOneCampaignDataset", methods=["POST"])
def createCountriesForOneCampaignDataset():
    campaign_id = request.json["campaignID"]
    date_range = request.json["dateRange"]
    return create_countries_for_one_campaign_dataset(date_range, campaign_id)

@app.route("/jsonapi/createCountriesForOneCampaignReport", methods=["POST"])
def createCountriesForOneCampaignReport():
    campaign_id = request.json["campaignID"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_countries_for_one_campaign_report(campaign_id, date_range, c1, c2, c3, c1Value, c2Value, c3Value)

#####################################
# languages for all campaigns

@app.route("/jsonapi/createLanguagesForAllCampaignsDataset", methods=["POST"])
def createLanguagesForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_languages_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createLanguagesForAllCampaignsReport", methods=["POST"])
def createLanguagesForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_languages_for_all_campaigns_report(date_range, c1, c2, c3, c1Value, c2Value, c3Value)

#####################################
# campaigns for one language 

@app.route("/jsonapi/createCampaignsForOneLanguageDataset", methods=["POST"])
def createCampaignsForOneLanguageDataset():
    language_name = request.json["languageName"]
    date_range = request.json["dateRange"]
    return create_campaigns_for_one_language_dataset(date_range, language_name)

@app.route("/jsonapi/createCampaignsForOneLanguageReport", methods=["POST"])
def createCampaignsForOneLanguageReport():
    language_name = request.json["languageName"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    return create_campaigns_for_one_language_report(language_name, date_range, c1, c2, c1Value, c2Value)

#####################################
# languages for one campaign

@app.route("/jsonapi/createLanguagesForOneCampaignDataset", methods=["POST"])
def createLanguagessForOneCampaignDataset():
    campaign_id = request.json["campaignID"]
    date_range = request.json["dateRange"]
    return create_languages_for_one_campaign_dataset(date_range, campaign_id)

@app.route("/jsonapi/createLanguagesForOneCampaignReport", methods=["POST"])
def createLanguagesForOneCampaignReport():
    campaign_id = request.json["campaignID"]
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    return create_languages_for_one_campaign_report(campaign_id, date_range, c1, c2, c3, c1Value, c2Value, c3Value)

#####################################
# days for one p widget for all campaigns

@app.route("/jsonapi/createDaysForOnePWidgetForAllCampaignsDataset", methods=["POST"])
def createDaysForOnePWidgetForAllCampaignsDataset():
    p_widget_id = request.json["pWidgetID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_p_widget_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, p_widget_id)

@app.route("/jsonapi/createDaysForOnePWidgetForAllCampaignsReport", methods=["POST"])
def createDaysForOnePWidgetForAllCampaignsReport():
    p_widget_id = request.json["pWidgetID"]
    return create_days_for_one_p_widget_for_all_campaigns_report(p_widget_id)

#####################################
# months for one p widget for all campaigns

@app.route("/jsonapi/createMonthsForOnePWidgetForAllCampaignsDataset", methods=["POST"])
def createMonthsForOnePWidgetForAllCampaignsDataset():
    p_widget_id = request.json["pWidgetID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_p_widget_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, p_widget_id)

@app.route("/jsonapi/createMonthsForOnePWidgetForAllCampaignsReport", methods=["POST"])
def createMonthsForOnePWidgetForAllCampaignsReport():
    p_widget_id = request.json["pWidgetID"]
    return create_months_for_one_p_widget_for_all_campaigns_report(p_widget_id)

#####################################
# days for one p widget for one campaign

@app.route("/jsonapi/createDaysForOnePWidgetForOneCampaignDataset", methods=["POST"])
def createDaysForOnePWidgetForOneCampaignDataset():
    p_widget_id = request.json["pWidgetID"]
    vol_id = request.json["volID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_p_widget_for_one_campaign_dataset(vol_token,
            vol_start_date, vol_end_date, p_widget_id, vol_id)

@app.route("/jsonapi/createDaysForOnePWidgetForOneCampaignReport", methods=["POST"])
def createDaysForOnePWidgetForOneCampaignReport():
    p_widget_id = request.json["pWidgetID"]
    vol_id = request.json["volID"]
    return create_days_for_one_p_widget_for_one_campaign_report(p_widget_id,
            vol_id)

#####################################
# months for one p widget for one campaign

@app.route("/jsonapi/createMonthsForOnePWidgetForOneCampaignDataset", methods=["POST"])
def createMonthsForOnePWidgetForOneCampaignDataset():
    p_widget_id = request.json["pWidgetID"]
    vol_id = request.json["volID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_p_widget_for_one_campaign_dataset(vol_token,
            vol_start_date, vol_end_date, p_widget_id, vol_id)

@app.route("/jsonapi/createMonthsForOnePWidgetForOneCampaignReport", methods=["POST"])
def createMonthsForOnePWidgetForOneCampaignReport():
    p_widget_id = request.json["pWidgetID"]
    vol_id = request.json["volID"]
    return create_months_for_one_p_widget_for_one_campaign_report(p_widget_id,
            vol_id)

#####################################
# days for one c widget for all campaigns

@app.route("/jsonapi/createDaysForOneCWidgetForAllCampaignsDataset", methods=["POST"])
def createDaysForOneCWidgetForAllCampaignsDataset():
    c_widget_id = request.json["cWidgetID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_c_widget_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, c_widget_id)

#####################################
# months for one c widget for all campaigns

@app.route("/jsonapi/createMonthsForOneCWidgetForAllCampaignsDataset", methods=["POST"])
def createMonthsForOneCWidgetForAllCampaignsDataset():
    c_widget_id = request.json["cWidgetID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_c_widget_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, c_widget_id)

@app.route("/jsonapi/createMonthsForOneCWidgetForAllCampaignsReport", methods=["POST"])
def createMonthsForOneCWidgetForAllCampaignsReport():
    c_widget_id = request.json["cWidgetID"]
    return create_months_for_one_c_widget_for_all_campaigns_report(c_widget_id)

#####################################
# days for one c widget for one campaign

@app.route("/jsonapi/createDaysForOneCWidgetForOneCampaignDataset", methods=["POST"])
def createDaysForOneCWidgetForOneCampaignDataset():
    c_widget_id = request.json["cWidgetID"]
    vol_id = request.json["volID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_c_widget_for_one_campaign_dataset(vol_token,
            vol_start_date, vol_end_date, c_widget_id, vol_id)

@app.route("/jsonapi/createDaysForOneCWidgetForOneCampaignReport", methods=["POST"])
def createDaysForOneCWidgetForOneCampaignReport():
    c_widget_id = request.json["cWidgetID"]
    vol_id = request.json["volID"]
    return create_days_for_one_c_widget_for_one_campaign_report(c_widget_id,
            vol_id)

#####################################
# months for one c widget for one campaign

@app.route("/jsonapi/createMonthsForOneCWidgetForOneCampaignDataset", methods=["POST"])
def createMonthsForOneCWidgetForOneCampaignDataset():
    c_widget_id = request.json["cWidgetID"]
    vol_id = request.json["volID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_c_widget_for_one_campaign_dataset(vol_token,
            vol_start_date, vol_end_date, c_widget_id, vol_id)

@app.route("/jsonapi/createMonthsForOneCWidgetForOneCampaignReport", methods=["POST"])
def createMonthsForOneCWidgetForOneCampaignReport():
    c_widget_id = request.json["cWidgetID"]
    vol_id = request.json["volID"]
    return create_months_for_one_c_widget_for_one_campaign_report(c_widget_id,
            vol_id)


#####################################
# days for one ad for all campaigns

@app.route("/jsonapi/createDaysForOneAdForAllCampaignsDataset", methods=["POST"])
def createDaysForOneAdForAllCampaignsDataset():
    ad_image = request.json["adImage"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_ad_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, ad_image) 

@app.route("/jsonapi/createDaysForOneAdForAllCampaignsReport", methods=["POST"])
def createDaysForOneAdForAllCampaignsReport():
    ad_image = request.json["adImage"]
    return create_days_for_one_ad_for_all_campaigns_report(ad_image)

#####################################
# months for one ad for all campaigns

@app.route("/jsonapi/createMonthsForOneAdForAllCampaignsDataset", methods=["POST"])
def createMonthsForOneAdForAllCampaignsDataset():
    ad_image = request.json["adImage"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_ad_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, ad_image)

@app.route("/jsonapi/createMonthsForOneAdForAllCampaignsReport", methods=["POST"])
def createMonthsForOneAdForAllCampaignsReport():
    ad_image = request.json["adImage"]
    return create_months_for_one_ad_for_all_campaigns_report(ad_image)

#####################################
# days for one ad for one campaign

@app.route("/jsonapi/createDaysForOneAdForOneCampaignDataset", methods=["POST"])
def createDaysForOneAdForOneCampaignDataset():
    print("here")
    ad_image = request.json["adImage"]
    vol_id = request.json["volID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_ad_for_one_campaign_dataset(vol_token,
            vol_start_date, vol_end_date, ad_image, vol_id)

@app.route("/jsonapi/createDaysForOneAdForOneCampaignReport", methods=["POST"])
def createDaysForOneAdForOneCampaignReport():
    ad_image = request.json["adImage"]
    vol_id = request.json["volID"]
    return create_days_for_one_ad_for_one_campaign_report(ad_image,
            vol_id)

#####################################
# months for one ad for one campaign

@app.route("/jsonapi/createMonthsForOneAdForOneCampaignDataset", methods=["POST"])
def createMonthsForOneAdForOneCampaignDataset():
    ad_image = request.json["adImage"]
    vol_id = request.json["volID"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_ad_for_one_campaign_dataset(vol_token,
            vol_start_date, vol_end_date, ad_image, vol_id)

@app.route("/jsonapi/createMonthsForOneAdForOneCampaignReport", methods=["POST"])
def createMonthsForOneAdForOneCampaignReport():
    ad_image = request.json["adImage"]
    vol_id = request.json["volID"]
    return create_months_for_one_ad_for_one_campaign_report(ad_image, vol_id)

#####################################
# days for one offer for all campaigns

@app.route("/jsonapi/createDaysForOneOfferForAllCampaignsDataset", methods=["POST"])
def createDaysForOneOfferForAllCampaignsDataset():
    offer_name = request.json["offerName"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_offer_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, offer_name) 

@app.route("/jsonapi/createDaysForOneOfferForAllCampaignsReport", methods=["POST"])
def createDaysForOneOfferForAllCampaignsReport():
    offer_name = request.json["offerName"]
    return create_days_for_one_offer_for_all_campaigns_report(offer_name)

#####################################
# months for one offer for all campaigns

@app.route("/jsonapi/createMonthsForOneOfferForAllCampaignsDataset", methods=["POST"])
def createMonthsForOneOfferForAllCampaignsDataset():
    offer_name = request.json["offerName"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_offer_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, offer_name)

@app.route("/jsonapi/createMonthsForOneOfferForAllCampaignsReport", methods=["POST"])
def createMonthsForOneOfferForAllCampaignsReport():
    offer_name = request.json["offerName"]
    return create_months_for_one_offer_for_all_campaigns_report(offer_name)

#####################################
# days for one country for all campaigns

@app.route("/jsonapi/createDaysForOneCountryForAllCampaignsDataset", methods=["POST"])
def createDaysForOneCountryForAllCampaignsDataset():
    country_name = request.json["countryName"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_days_for_one_country_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, country_name) 

@app.route("/jsonapi/createDaysForOneCountryForAllCampaignsReport", methods=["POST"])
def createDaysForOneCountryForAllCampaignsReport():
    country_name = request.json["countryName"]
    return create_days_for_one_country_for_all_campaigns_report(country_name)

#####################################
# months for one country for all campaigns

@app.route("/jsonapi/createMonthsForOneCountryForAllCampaignsDataset", methods=["POST"])
def createMonthsForOneCountryForAllCampaignsDataset():
    country_name = request.json["countryName"]
    vol_token = get_vol_access_token(vol_access_id, vol_access_key)
    vol_dates = create_vol_date_range(180, mgid_timezone)
    vol_start_date = vol_dates[0]
    vol_end_date = vol_dates[1]
    return create_months_for_one_country_for_all_campaigns_dataset(vol_token,
            vol_start_date, vol_end_date, country_name)

@app.route("/jsonapi/createMonthsForOneCountryForAllCampaignsReport", methods=["POST"])
def createMonthsForOneCountryForAllCampaignsReport():
    country_name = request.json["countryName"]
    return create_months_for_one_country_for_all_campaigns_report(country_name)

#####################################
# days for one campaign

@app.route("/jsonapi/createDaysForOneCampaignReport", methods=["POST"])
def createDaysForOneCampaignReport():
    vol_id = request.json["volid"]
    return create_days_for_one_campaign_report(vol_id)

#####################################
# gprs for each p widget

@app.route("/jsonapi/createGprsForEachPOfferDataset", methods=["POST"])
def createGprsForEachPOfferDataset():
    date_range = request.json["dateRange"]
    return create_gprs_for_each_p_offer_dataset(date_range)


if __name__ == '__main__':
    app.run(port=5001, debug=True)

