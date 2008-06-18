dmm1 = qt.instruments.create('dmm1', 'example', address='GPIB::1')
dsgen = qt.instruments.create('dsgen', 'dummy_signal_generator')
combined = qt.instruments.create('combined', 'virtual_composite')
combined.add_variable_scaled('magnet', dmm1, 'ch1_output', 0.02, -0.13, units='mT')
combined.add_variable_combined('waveoffset', [{
    'instrument': dmm1,
    'parameter': 'ch2_output',
    'scale': 1,
    'offset': 0}, {
    'instrument': dsgen,
    'parameter': 'wave',
    'scale': 0.5,
    'offset': 0
    }], format='%.04f')
