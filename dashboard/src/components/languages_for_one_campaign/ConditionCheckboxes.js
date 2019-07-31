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
        <span>Language classification is </span>
        <select
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="good">good</option>
          <option value="bad">bad</option>
          <option value="wait">wait</option>
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
        <span>
          {'Language cost is greater than or equal to $'}
          <input
            type="number"
            name="c2Value"
            min="0"
            max="1000"
            step="10"
            value={c2Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
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
          {'Language loss is greater than or equal to $'}
          <input
            type="number"
            name="c3Value"
            min="50"
            max="500"
            step="10"
            value={c3Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
