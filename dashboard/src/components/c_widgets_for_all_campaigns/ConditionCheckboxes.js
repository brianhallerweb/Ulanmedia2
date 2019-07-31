//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({
  toggleCondition,
  setConditionValue,
  loading,
  c1,
  c1Value,
  c2,
  c2Value,
  c3,
  c3Value,
  c4,
  c4Value,
  c5,
  c5Value,
  c6,
  c6Value,
  c7,
  c8,
}) => {
  return (
    <div style={{paddingTop: 15, paddingBottom: 15}}>
      <div>
        <input
          type="checkbox"
          name="c1"
          checked={c1}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Widget classification is </span>
        <select
          disabled={loading}
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="wait">wait</option>
          <option value="white">white</option>
          <option value="black">black</option>
          <option value="grey">grey</option>
        </select>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Widget global status is </span>
        <select
          disabled={loading}
          onChange={e => setConditionValue('c2Value', e.target.value)}
          defaultValue={c2Value}>
          <option value="waiting">waiting</option>
          <option value="pc_whitelist">pc_whitelist</option>
          <option value="pc_greylist">pc_greylist</option>
          <option value="pc_blacklist">pc_blacklist</option>
          <option value="p_whitelist">p_whitelist</option>
          <option value="p_greylist">p_greylist</option>
          <option value="p_blacklist">p_blacklist</option>
          <option value="c_whitelist">c_whitelist</option>
          <option value="c_greylist">c_greylist</option>
          <option value="c_blacklist">c_blacklist</option>
        </select>
      </div>

      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget cost is greater than or equal to $'}
          <input
            disabled={loading}
            className="inputBox"
            type="number"
            name="c3Value"
            min="0"
            max="100"
            step="1"
            value={c3Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' (warning, unchecking may cause browser to crash)'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c4"
          checked={c4}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget loss is greater than or equal to $'}
          <input
            className="inputBox"
            type="number"
            name="c4Value"
            min="0"
            max="100"
            step="1"
            value={c4Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget leads is greater than or equal to '}
          <input
            className="inputBox"
            type="number"
            name="c5Value"
            min="0"
            max="1000"
            step="1"
            value={c5Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget sales is greater than or equal to '}
          <input
            className="inputBox"
            type="number"
            name="c6Value"
            min="0"
            max="1000"
            step="1"
            value={c6Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c7"
          checked={c7}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        Widget has included bad campaigns
      </div>

      <div>
        <input
          type="checkbox"
          name="c8"
          checked={c8}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        Widget classification doesn't match global status
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
