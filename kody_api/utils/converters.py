
from typing import Any, Dict
from sqlalchemy.engine.row import Row


def row_to_json(r: Row) -> Dict[str, Any]:
    """Gera um JSON a partir de uma Row, oriunda de um query do SQLAlchemy.

    Args:
        r (Row): Resultado de uma query

    Returns:
        Dict[str, Any]: JSON da query
    """
    return {n.lower(): v.__dict__ if hasattr(v, "__dict__") else v for n, v in zip(r.keys(), r)}
