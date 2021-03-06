Reading data files
==================

Data is available in *trains*, which arrive ten times per second.
Each train has a unique train ID, which is used to match up corresponding data
stored separately. Many data sources will make one reading per train, but some,
including the main detectors, record data more frequently.

.. module:: karabo_data

.. autoclass:: RunDirectory

   .. attribute:: train_ids

      A list of the train IDs for which there is any data in this run.
      The data recorded may not be the same for each train.

   .. attribute:: control_sources

      A set of the control source names in this run, in the format
      ``"SA3_XTD10_VAC/TSENS/S30100K"``.

   .. attribute:: instrument_sources

      A set of the instrument source names in this run,
      in the format ``"FXE_DET_LPD1M-1/DET/15CH0:xtdf"``.

   .. automethod:: trains

   .. automethod:: train_from_id

   .. automethod:: train_from_index

   .. automethod:: get_dataframe

   .. automethod:: get_series

   .. automethod:: get_array


.. autoclass:: H5File

   .. attribute:: train_ids

      A list of the train IDs for which there is data in this file.

   .. attribute:: control_sources

      A set of the control source names in this run, in the format
      ``"SA3_XTD10_VAC/TSENS/S30100K"``.

   .. attribute:: instrument_sources

      A set of the instrument source names in this run,
      in the format ``"FXE_DET_LPD1M-1/DET/15CH0:xtdf"``.

   .. automethod:: trains

   .. automethod:: train_from_id

   .. automethod:: train_from_index

   .. automethod:: get_dataframe

   .. automethod:: get_series

   .. automethod:: get_array
