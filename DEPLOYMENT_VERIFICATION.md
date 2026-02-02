# Thalos Prime Deployment Verification

## Pre-Deployment Checklist

### 1. Run Verification Script
```bash
python verify_deployment.py
```

**Expected Output**:
```
✓ Critical Files: PASS
✓ Critical Imports: PASS  
✓ CIS Boot: PASS
✓ ConversationEngine: PASS

🎉 ALL VERIFICATIONS PASSED!
```

### 2. Test Boot Sequence
```bash
python boot_thalos.py
```

**Expected Behavior**:
- Dependencies checked/installed
- CIS initializes successfully
- Web server starts on port 8000
- Browser opens to Matrix interface
- Chat responds to input

### 3. Manual Testing

**Test in Browser** (http://localhost:8000):
1. Type: "Hello" → Expect greeting response
2. Type: "status" → Expect system status
3. Type: "memory" → Expect memory info
4. Type: "help" → Expect command list

### 4. Verify No Import Errors

```bash
python -c "import sys; sys.path.insert(0, 'src'); from interfaces.chatbot.conversation import ConversationEngine; print('✓ ConversationEngine import OK')"
```

---

## Common Issues

### Issue: ImportError: No module named 'interfaces.chatbot.conversation'
**Solution**: Ensure `src/interfaces/chatbot/conversation.py` exists (created in this PR)

### Issue: NameError: name 'datetime' is not defined
**Solution**: Add `from datetime import datetime` to `immersive_server.py` (fixed in this PR)

### Issue: Web server won't start
**Solution**: Check port 8000 is available: `lsof -i :8000` (Unix) or `netstat -ano | findstr :8000` (Windows)

---

## Deployment Success Criteria

✅ `verify_deployment.py` passes all tests  
✅ `boot_thalos.py` launches without errors  
✅ Web interface accessible at http://localhost:8000  
✅ Chat responds to user input  
✅ No ImportError or NameError exceptions  
✅ System shutdown gracefully with Ctrl+C  

---

**VERIFICATION PHILOSOPHY**:  
"A system that cannot verify itself deterministically cannot claim operational status."
