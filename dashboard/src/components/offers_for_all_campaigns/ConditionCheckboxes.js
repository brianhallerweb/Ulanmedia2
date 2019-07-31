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
        <span>Offer classification is </span>
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
          {'Offer cost is greater than or equal to $'}
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
          {'Offer loss is greater than or equal to $'}
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

      <div>
        <input
          type="checkbox"
          name="c4"
          checked={c4}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Lead CVR is less than or equal to '}
          <input
            type="number"
            name="c4Value"
            min="0"
            max=".50"
            step=".01"
            value={c4Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'%'}
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
        Voluum weight doesn't match recommended weight
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
