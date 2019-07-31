//@format
import React, {Component} from 'react';

const FixedValueCheckbox = ({
  conditionName,
  condition,
  label,
  toggleCondition,
  disabled,
}) => (
  <div>
    <input
      type="checkbox"
      name={conditionName}
      checked={condition}
      disabled={disabled}
      onChange={e => toggleCondition(e.target.name)}
    />
    <span>{label}</span>
  </div>
);

export default FixedValueCheckbox;
