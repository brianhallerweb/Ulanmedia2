//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';
import VariableValueCheckbox from '../utilities/VariableValueCheckbox';
import FixedValueCheckbox from '../utilities/FixedValueCheckbox';

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
  c5,
  c6,
  c6Value,
  c7,
  c7Value,
  c8,
  c8Value,
  c9,
  c9Value,
  c10,
  c10Value,
  c11,
  c11Value,
  c12,
  c12Value,
  c13,
  c13Value,
  c14,
  c14Value,
  c15,
  c15Value,
  c16,
  c16Value,
  c17,
  c17Value,
  c18,
  c18Value,
  c19,
  c19Value,
  c20,
  c20Value,
  c21,
  c21Value,
  c22,
  c22Value,
  c23,
  c23Value,
  c24,
  c24Value,
  c25,
  c25Value,
  c26,
  c26Value,
  c27,
  c27Value,
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
        <span>Campaign classification is </span>
        <select
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="wait">wait</option>
          <option value="good">good</option>
          <option value="bad">bad</option>
        </select>
      </div>
      <VariableValueCheckbox
        conditionName={'c2'}
        condition={c2}
        conditionValueName={'c2Value'}
        conditionValue={c2Value}
        label1={'Campaign cost is greater than or equal to $'}
        label2={''}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c3'}
        condition={c3}
        conditionValueName={'c3Value'}
        conditionValue={c3Value}
        label1={'Campaign loss is greater than or equal to $'}
        label2={''}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <FixedValueCheckbox
        conditionName={'c4'}
        condition={c4}
        label={'Campaign has sales'}
        toggleCondition={toggleCondition}
        disabled={loading}
      />
      <FixedValueCheckbox
        conditionName={'c5'}
        condition={c5}
        label={"Campaign doesn't have sales"}
        toggleCondition={toggleCondition}
        disabled={loading}
      />
      <p>-----------------------------------------------------</p>
      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower cost or tighten targeting:
      </p>
      <VariableValueCheckbox
        conditionName={'c6'}
        condition={c6}
        conditionValueName={'c6Value'}
        conditionValue={c6Value}
        label1={'Campaign bid is greater than or equal to EPC plus '}
        label2={'% [bid >= EPC+(EPC*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c7'}
        condition={c7}
        conditionValueName={'c7Value'}
        conditionValue={c7Value}
        label1={'Campaign CPC is greater than or equal to EPC plus '}
        label2={'% [CPC >= EPC+(EPC*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c8'}
        condition={c8}
        conditionValueName={'c8Value'}
        conditionValue={c8Value}
        label1={'Campaign CPL is greater than or equal to EPL plus '}
        label2={'% [CPL >= EPL+(EPL*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c9'}
        condition={c9}
        conditionValueName={'c9Value'}
        conditionValue={c9Value}
        label1={'Campaign CPS is greater than or equal to EPS plus '}
        label2={'% [CPS >= EPS+(EPS*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise cost or loosen targeting:
      </p>
      <VariableValueCheckbox
        conditionName={'c10'}
        condition={c10}
        conditionValueName={'c10Value'}
        conditionValue={c10Value}
        label1={'Campaign bid is less than or equal to EPC minus '}
        label2={'% [bid <= EPC-(EPC*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c11'}
        condition={c11}
        conditionValueName={'c11Value'}
        conditionValue={c11Value}
        label1={'Campaign CPC is less than or equal to EPC minus '}
        label2={'% [CPC <= EPC-(EPC*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c12'}
        condition={c12}
        conditionValueName={'c12Value'}
        conditionValue={c12Value}
        label1={'Campaign CPL is less than or equal to EPL minus '}
        label2={'% [CPL <= EPL-(EPL*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c13'}
        condition={c13}
        conditionValueName={'c13Value'}
        conditionValue={c13Value}
        label1={'Campaign CPS is less than or equal to EPS minus '}
        label2={'% [CPS <= EPS-(EPS*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <p>-----------------------------------------------------</p>
      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower cost or tighten targeting or raise max per
        click/lead/sale:
      </p>
      <VariableValueCheckbox
        conditionName={'c14'}
        condition={c14}
        conditionValueName={'c14Value'}
        conditionValue={c14Value}
        label1={'Campaign bid is greater than or equal to MPC plus '}
        label2={'% [bid >= MPC+(MPC*0)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c15'}
        condition={c15}
        conditionValueName={'c15Value'}
        conditionValue={c15Value}
        label1={'Campaign CPC is greater than or equal to MPC plus '}
        label2={'% [CPC >= MPC+(MPC*0)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />

      <VariableValueCheckbox
        conditionName={'c16'}
        condition={c16}
        conditionValueName={'c16Value'}
        conditionValue={c16Value}
        label1={
          'Campaign CPL or Cost(no leads) is greater than or equal to MPL plus '
        }
        label2={
          '% [CPL >= MPL+(MPL*0)] or [leads == 0 AND Cost >= MPL+(MPL*0)]'
        }
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c17'}
        condition={c17}
        conditionValueName={'c17Value'}
        conditionValue={c17Value}
        label1={
          'Campaign CPS or Cost(no sales) is greater than or equal to MPS plus '
        }
        label2={
          '% [CPS >= MPS+(MPS*0)] or [sales == 0 AND Cost >= MPS+(MPS*0)]'
        }
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise cost or loosen targeting or lower max per click/lead/sale:
      </p>
      <VariableValueCheckbox
        conditionName={'c18'}
        condition={c18}
        conditionValueName={'c18Value'}
        conditionValue={c18Value}
        label1={'Campaign bid is less than or equal to MPC minus '}
        label2={'% [bid <= MPC-(MPC*0)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c19'}
        condition={c19}
        conditionValueName={'c19Value'}
        conditionValue={c19Value}
        label1={'Campaign CPC is less than or equal to MPC minus '}
        label2={'% [CPC <= MPC-(MPC*0)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c20'}
        condition={c20}
        conditionValueName={'c20Value'}
        conditionValue={c20Value}
        label1={'Campaign CPL is less than or equal to MPL minus '}
        label2={'% [CPL <= MPL-(MPL*0)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c21'}
        condition={c21}
        conditionValueName={'c21Value'}
        conditionValue={c21Value}
        label1={'Campaign CPS is less than or equal to MPS minus '}
        label2={'% [CPS <= MPS-(MPS*0)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <p>-----------------------------------------------------</p>
      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower max per click/lead/sale:
      </p>
      <VariableValueCheckbox
        conditionName={'c22'}
        condition={c22}
        conditionValueName={'c22Value'}
        conditionValue={c22Value}
        label1={'Campaign MPC is greater than or equal to EPC plus '}
        label2={'% [MPC >= EPC+(EPC*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c23'}
        condition={c23}
        conditionValueName={'c23Value'}
        conditionValue={c23Value}
        label1={'Campaign MPL is greater than or equal to EPL plus '}
        label2={'% [MPL >= EPL+(EPL*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c24'}
        condition={c24}
        conditionValueName={'c24Value'}
        conditionValue={c24Value}
        label1={'Campaign MPS is greater than or equal to EPS plus '}
        label2={'% [MPS >= EPS+(EPS*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise max per click/lead/sale:
      </p>
      <VariableValueCheckbox
        conditionName={'c25'}
        condition={c25}
        conditionValueName={'c25Value'}
        conditionValue={c25Value}
        label1={'Campaign MPC is less than or equal to EPC minus '}
        label2={'% [MPC <= EPC-(EPC*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c26'}
        condition={c26}
        conditionValueName={'c26Value'}
        conditionValue={c26Value}
        label1={'Campaign MPL is less than or equal to EPL minus '}
        label2={'% [MPL <= EPL-(EPS*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <VariableValueCheckbox
        conditionName={'c27'}
        condition={c27}
        conditionValueName={'c27Value'}
        conditionValue={c27Value}
        label1={'Campaign MPS is less than or equal to EPS minus '}
        label2={'% [MPS <= EPS-(EPS*0.30)]'}
        toggleCondition={toggleCondition}
        setConditionValue={setConditionValue}
        disabled={loading}
        min={'0'}
        max={'1000'}
        step={'1'}
      />
      <p>-----------------------------------------------------</p>
    </div>
  );
};

export default ConditionCheckboxes;
