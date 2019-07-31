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
          disabled={true}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Max recommended bid $'}
          <input
            className="inputBox"
            type="number"
            name="c1Value"
            min="0"
            max="10"
            step=".01"
            value={c1Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          disabled={true}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Default recommended coefficient if no sales and no leads '}
          <input
            className="inputBox"
            type="number"
            name="c2Value"
            min="0"
            max="10"
            step=".1"
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
          {'Widget cost is greater than or equal to $'}
          <input
            className="inputBox"
            type="number"
            name="c3Value"
            min="0"
            max="100"
            step="1"
            value={c3Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
