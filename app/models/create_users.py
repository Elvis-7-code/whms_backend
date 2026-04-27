from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    # Create database tables if they don't exist
    db.create_all()
    
    # Check if admin already exists
    if User.query.filter_by(email="admin@farm.com").first():
        print("⚠️  Admin already exists!")
    else:
        # Create admin user
        admin = User(
            name="Farm Admin",
            email="admin@farm.com",
            role="owner"
        )
        admin.set_password("Admin@123")
        db.session.add(admin)
    
    # Create manager
    if not User.query.filter_by(email="manager@farm.com").first():
        manager = User(
            name="Farm Manager",
            email="manager@farm.com",
            role="manager"
        )
        manager.set_password("Manager@123")
        db.session.add(manager)
    
    # Create worker
    if not User.query.filter_by(email="worker@farm.com").first():
        worker = User(
            name="Farm Worker",
            email="worker@farm.com",
            role="worker"
        )
        worker.set_password("Worker@123")
        db.session.add(worker)
    
    try:
        db.session.commit()
        print("\n✅ Users created successfully!\n")
        print("=" * 50)
        print("LOGIN CREDENTIALS:")
        print("=" * 50)
        print("Admin:   admin@farm.com    / Admin@123")
        print("Manager: manager@farm.com  / Manager@123")
        print("Worker:  worker@farm.com   / Worker@123")
        print("=" * 50)
    except Exception as e:
        print(f"❌ Error: {e}")
        db.session.rollback()