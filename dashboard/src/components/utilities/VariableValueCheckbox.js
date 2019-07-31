//@format
import React, {Component} from 'react';

const VariableValueCheckbox = ({
  conditionName,
  condition,
  conditionValueName,
  conditionValue,
  label1,
  label2,
  toggleCondition,
  setConditionValue,
  disabled,
  min,
  max,
  step,
}) => (
  <div>
    <input
      type="checkbox"
      name={conditionName}
      checked={condition}
      disabled={disabled}
      onChange={e => toggleCondition(e.target.name)}
    />
    <span>
      {label1}
      <input
        className="inputBox"
        type="number"
        name={conditionValueName}
        disabled={disabled}
        min={min}
        max={max}
        step={step}
        value={conditionValue}
        onChange={e => setConditionValue(e.target.name, e.target.value)}
      />
      {label2}
    </span>
  </div>
);

export default VariableValueCheckbox;
