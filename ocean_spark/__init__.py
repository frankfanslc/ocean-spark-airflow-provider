from typing import Dict
import ocean_spark.hooks
import ocean_spark.operators
import ocean_spark.extra_links


def get_provider_info() -> Dict:
    return {
        "package-name": "ocean-spark-airflow-provider",
        "name": "Ocean for Spark Airflow Provider",
        "description": "TODO(crezvoy): add description",
        "hook-class-names": ["ocean_spark.hooks.OceanSparkHook"],
        "connection-types": [
            {
                "hook-class-name": "ocean_spark.hooks.OceanSparkHook",
                "connection-type": "ocean_spark",
            },
        ],
        "extra-links": ["ocean_spark.extra_links.OceanSparkApplicationOverviewLink"],
    }
