//@format
import React, {Component} from 'react';

class AddCampaignSet extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  handleAdd(e) {
    e.preventDefault();
    const volCampaignID = e.target.elements.volCampaignID.value.trim();
    const mgidCampaignID = e.target.elements.mgidCampaignID.value.trim();
    const campaignName = e.target.elements.campaignName.value.trim();
    const maxLeadCPA = e.target.elements.maxLeadCPA.value.trim();
    const maxSaleCPA = e.target.elements.maxSaleCPA.value.trim();
    const campaignStatus = e.target.elements.campaignStatus.value.trim();
    this.props.handleAdd({
      volCampaignID,
      mgidCampaignID,
      campaignName,
      maxLeadCPA,
      maxSaleCPA,
      campaignStatus,
    });
    e.target.elements.volCampaignID.value = '';
    e.target.elements.mgidCampaignID.value = '';
    e.target.elements.campaignName.value = '';
    e.target.elements.maxLeadCPA.value = '';
    e.target.elements.maxSaleCPA.value = '';
    e.target.elements.campaignStatus.value = '';
  }

  render() {
    return (
      <div>
        {this.state.error && (
          <p className="add-widget-error">{this.state.error}</p>
        )}
        <form className="add-widget" onSubmit={this.handleAdd.bind(this)}>
          <div>
            <label>vol campaign id</label>
          </div>
          <div>
            <input
              className="add-widget__input"
              type="text"
              name="volCampaignID"
            />
          </div>
          <div>
            <label>mgid campaign id</label>
          </div>
          <div>
            <input
              className="add-widget__input"
              type="text"
              name="mgidCampaignID"
            />
          </div>
          <div>
            <label>campaign name</label>
          </div>
          <div>
            <input
              className="add-widget__input"
              type="text"
              name="campaignName"
            />
          </div>
          <div>
            <label>max lead cpa</label>
          </div>
          <div>
            ${' '}
            <input
              className="add-widget__input"
              type="text"
              name="maxLeadCPA"
              size="1"
            />
          </div>
          <div>
            <label>max sale cpa</label>
          </div>
          <div>
            ${' '}
            <input
              className="add-widget__input"
              type="text"
              name="maxSaleCPA"
              size="1"
            />
          </div>
          <div>
            <label>campaign status</label>
          </div>
          <div>
            <input
              className="add-widget__input"
              type="text"
              name="campaignStatus"
            />
          </div>
          <button style={{marginTop: 5}} className="button">
            Add campaign set
          </button>
        </form>
      </div>
    );
  }
}

export default AddCampaignSet;
