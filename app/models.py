from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Preprint(db.Model):
    __tablename__ = 'preprints'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    authors: so.Mapped[str] = so.mapped_column(sa.String(140), index=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(140), index=True)
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    preprint_id_per_year: so.Mapped[int] = so.mapped_column(index=True)
    preprint_id: so.Mapped[str] = so.mapped_column(sa.String(11), index=True, unique=True)

    def set_preprint_id(self, id):
        year = abs(datetime.now(timezone.utc).year) % 100
        strings = ['MITP', str(year), '{:03d}'.format(id)]
        self.preprint_id_per_year = id
        self.preprint_id = '-'.join(strings)

    def __repr__(self):
        return '<Preprint {}>'.format(self.preprint_id)